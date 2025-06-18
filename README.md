# PySide6 계산기 프로젝트

간단한 계산기 GUI 애플리케이션을 PySide6와 TDD(Test-Driven Development) 방식으로 개발합니다.

## 프로젝트 구조(초기)

```
practice/
  ├── main.py           # 메인 실행 파일(임시)
  ├── README.md         # 프로젝트 설명
  ├── tests/            # 테스트 코드 디렉토리
  └── calculator/       # 계산기 비즈니스 로직 및 GUI 코드
```

## 개발 방식
- PySide6 기반 GUI
- 모든 기능은 테스트 코드 작성 후 구현(TDD)
- 테스트 통과 코드만 반영
- 주요 변경/신규 기능은 README에 기록

## 실행 방법

```bash
python main.py
```

## 의존성 설치

numpy 등 추가 패키지가 필요하다면 아래 명령어로 설치하세요.

```bash
pip install numpy
```