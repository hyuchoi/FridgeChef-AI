import base64
import os

import streamlit as st
from openai import OpenAI

# -----------------------
# Page Config
# -----------------------

st.set_page_config(
    page_title="FridgeChef AI",
    page_icon="🍳",
    layout="wide"
)

# -----------------------
# API KEY
# -----------------------

api_key = st.secrets.get("OPENAI_API_KEY", None)

if api_key is None:
    st.error("OPENAI_API_KEY가 설정되지 않았습니다.")
    st.stop()

client = OpenAI(api_key=api_key)

# -----------------------
# HEADER
# -----------------------

st.title("🍳 FridgeChef AI")

st.caption(
    "냉장고 속 재료만으로 최고의 한 끼를 추천해주는 AI 셰프"
)

st.divider()

# -----------------------
# INPUT
# -----------------------

left, right = st.columns(2)

with left:

    st.subheader("🥕 재료 입력")

    ingredients = st.text_area(
        "가지고 있는 재료를 입력하세요",
        placeholder="""
예시)

계란
양파
햄
참치
치즈
김치
""",
        height=220
    )

with right:

    st.subheader("📷 냉장고 사진")

    uploaded_file = st.file_uploader(
        "사진 업로드",
        type=["jpg", "jpeg", "png"]
    )

st.divider()

recommend = st.button(
    "🍳 추천받기",
    use_container_width=True
)

# -----------------------
# PROMPT
# -----------------------

SYSTEM_PROMPT = """
당신은 세계 최고의 셰프이다.

사용자가 입력한 재료 또는 냉장고 사진을 분석한다.

항상 아래 형식으로 답한다.

🍳 추천 요리

🥬 사용 재료

🛒 부족한 재료

👨‍🍳 만드는 방법

⏰ 조리시간

⭐ 난이도

🔥 예상 칼로리

🥗 영양정보

🛍 쇼핑 리스트

🍽 다음 식단 추천

가능하면
- 음식물 쓰레기를 줄이는 방법
- 현재 재료를 최대한 활용
- 부족한 재료 최소화
- 한국식 우선
- 쉽고 간단한 레시피
"""

# -----------------------
# IMAGE
# -----------------------

def image_to_base64(upload):

    return base64.b64encode(upload.read()).decode("utf-8")

# -----------------------
# GPT
# -----------------------

if recommend:

    if ingredients == "" and uploaded_file is None:

        st.warning("재료 또는 사진을 입력해주세요.")

        st.stop()

    with st.spinner("🍳 최고의 요리를 찾는 중..."):

        content = []

        if ingredients != "":

            content.append(
                {
                    "type":"input_text",
                    "text":f"재료:\n{ingredients}"
                }
            )

        if uploaded_file:

            image_data = image_to_base64(uploaded_file)

            content.append(
                {
                    "type":"input_image",
                    "image_url":f"data:image/jpeg;base64,{image_data}"
                }
            )

        response = client.responses.create(

            model="gpt-5.5",

            instructions=SYSTEM_PROMPT,

            input=[
                {
                    "role":"user",
                    "content":content
                }
            ]

        )

    st.success("추천 완료!")

    st.markdown(response.output_text)