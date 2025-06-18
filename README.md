# PySide6 계산기 프로젝트

간단한 계산기 GUI 애플리케이션을 PySide6와 TDD(Test-Driven Development) 방식으로 개발합니다.

## 프로젝트 구조

```
practice/
  ├── main.py                 # 메인 실행 파일(임시)
  ├── README.md               # 프로젝트 설명
  ├── tests/                  # 테스트 코드 디렉토리
  │    ├── test_sample.py         # 샘플 테스트 코드
  │    └── test_calculator.py     # 계산기 기능 테스트 코드
  └── calculator/             # 계산기 비즈니스 로직 및 GUI 코드
       └── calc.py            # 계산 로직 (add, sub, mul, div 등)
```

## 주요 기능
- 덧셈, 뺄셈, 곱셈, 나눗셈 연산 지원
- 0으로 나누기 등 예외 상황 처리
- 모든 기능은 테스트 코드(TDD) 기반으로 구현

## 개발 및 실행 방법
1. 의존성 설치
   ```bash
   pip install pyside6 pytest
   ```
2. 테스트 실행
   ```bash
   pytest
   ```
3. (향후) main.py 또는 calculator/ 내 GUI 실행 코드로 계산기 실행

## 테스트
- `tests/test_calculator.py`에서 모든 연산 및 예외 테스트가 구현되어 있음
- 모든 테스트가 통과해야 코드가 반영됨

## 개발 규칙 및 워크플로우
- `.cursor/rules/project-rule.mdc`와 `.cursor/rules/workflow-calculator.md` 참고
- TDD, README 업데이트, 체크리스트 관리 등 엄격히 준수