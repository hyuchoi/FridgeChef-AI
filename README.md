# 🍳 FridgeChef AI

FridgeChef AI는 냉장고 속 재료나 냉장고 사진을 기반으로 만들 수 있는 요리를 추천해주는 AI 서비스입니다.

## 주요 기능

* 📷 냉장고 사진 분석
* 🥕 재료 입력
* 🍳 맞춤 요리 추천
* 🥗 영양 정보 제공
* 🛒 부족한 재료 및 쇼핑리스트 생성
* 🍽 다음 식단 추천

## 실행 방법

```bash
pip install -r requirements.txt
streamlit run app.py
```

## API Key 설정

`.streamlit/secrets.toml`

```toml
OPENAI_API_KEY="YOUR_API_KEY"
```

## Streamlit Community Cloud 배포

1. GitHub에 이 프로젝트를 푸시합니다.
2. Streamlit Community Cloud에 로그인합니다.
3. 새 앱을 만들고 GitHub 리포지토리를 연결합니다.
4. `OPENAI_API_KEY`를 앱 시크릿으로 설정합니다.
5. 앱을 배포합니다.

> `.streamlit/secrets.toml`은 절대로 깃에 커밋하지 마세요. 배포할 때는 Streamlit Cloud의 Secrets 설정을 사용하세요.
