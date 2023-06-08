from typing import List
import re
import collections

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    # 구두점 무시하기 위해 정규표현식 사용
    # r은 Raw String (원시 문자열)을 나타내는 접두사 
    # 파이썬에서 Raw String은 백슬래시 \를 이스케이프 시키지 않고 그대로 사용할 수 있도록 해줌
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split() 
             if word not in banned]

    # counts = collections.defaultdict(int)
    # for word in words:
    #     counts[word] += 1

    # return max(counts, key=counts.get)

    counts = collections.Counter(words) # Counter 객체

    return counts.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(mostCommonWord(paragraph, banned))