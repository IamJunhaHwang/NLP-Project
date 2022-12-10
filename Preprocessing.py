import re

def preprocess(text: str, only_kor: bool = True):
    """한국어 문장을 옵션에 맞게 전처리"""
    # 한국어 모음과 특수 문자, 숫자 및 영어 제거
    if only_kor:
        text = re.sub(f"[^가-힣| |]+", "", text)
    else:
        text = re.sub(f"[^가-힣|ㄱ-ㅎ|0-9|]+", "", text)

    # 연속 공백 제거
    text = re.sub(" +", " ", text)

    # 좌우 불필요한 공백 제거
    return text.strip()

if __name__ == "__main__":
    sample_sen = "DLP 계열의 옵토마와 3LCD 방식의 엡손제품 5개 모델을 사용해 보았지만 ++ 이게 제일 괜찮더라~~!"

    print(preprocess(sample_sen, True))

    # 결과: 계열의 옵토마와 방식의 엡손제품 개 모델을 사용해 보았지만 이게 제일 괜찮더라