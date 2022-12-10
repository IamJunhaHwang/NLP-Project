## NLP-Project

해당 레포지토리는 `자연언어처리` 과목의 일환으로 만들어졌습니다.

[2022 국립국어원 인공 지능 언어 능력 평가](https://corpus.korean.go.kr/task/taskList.do?taskId=8&clCd=END_TASK&subMenuId=sub01) 태스크에 참가하고 이를 해결하는 방법을 구현합니다.

---------

### 의존성

파이썬 라이브러리 설치는 아래와 같이 진행하면 됩니다. [git clone이 필요합니다]

  ```bash
  pip install -r requirements.txt
  ```

--------

### 모델 설명

해당 태스크를 해결하기 위해 2가지 종류의 모델이 생성됩니다. 하나는 태그 추출을 위한 모델이고 다른 하나는 감성 분석을 위한 모델입니다.

두 모델 모두 `klue-RoBERTa-large` 모델을 base로 하며, 해당 모델 위에 `Linear Layer`를 하나를 더 두는 구조로 만들어졌습니다.

- 태그 추출 모델

  - 태그 추출은 각 태그에 대한 모델을 생성하여 각각의 모델이 자신이 맡은 태그에 대해 문장에 그 특성이 나타는지 True/False를 예측하는 모델입니다.
  
  - 즉, 어떠한 문장에 대해 특정 태그가 추출되느냐 안되느냐를 예측합니다.
  
  - 입력으로는 하나의 문장이 들어가고 해당 문장에 대해 각 모델들이 태그가 추출될지를 예측합니다.
  
- 감성 분석 모델

  - 감성 분석 모델은 `문장 + 태그`를 입력으로 받아 해당 입력에 대한 감성을 예측합니다. [감성은 긍정, 부정, 중립으로 3가지입니다]
  
  - 입력인 `문장 + 태그`에 대해서는 추론 시에 태그 추출 모델이 예측해 낸(True를 반환한) 태그를 붙여줍니다.
  
  - 감성 분석 모델의 경우 입력에 `태그`가 들어가기 때문에 `Tokenizer`에 태그들을 `SPECIAL_TOKENS`로 설정하였으며 해당 모델의 `Embedding_Layer`와 `Vocab_size` 또한 이에 맞게 Resize 되었습니다.

------

### 사용 데이터

모델 생성에 사용된 데이터는 아래와 같습니다.

- **속성 기반 감성 분석 데이터**

  - 데이터 출처: [모두의 말뭉치](https://corpus.korean.go.kr/main.do)
  
  - 데이터명: 인공지능 언어 능력 평가: 속성 기반 감성 분석(버전1.0)
  
--------
  
### 라이선스

This project following Apache 2.0 License as written in LICENSE file

Copyright 2022 JunHa-Hwang and klue contributors

Copyright (c) 2021 KLUE-baseline : KLUE-baseline

### Author

- JunHa-Hwang, hwang_junha@naver.com, ChungBuk National Univ(Undergraduate).
