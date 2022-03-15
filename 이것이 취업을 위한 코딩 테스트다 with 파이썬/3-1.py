# key point
# 가지고 있는 동전들의 큰 단위가 항상 작은 단위의 배수라는 게 중요
# 작은 단위의 동전들을 종합해 다른 해가 나올 수가 없음
# 따라서 큰 단위의 동전 먼저 계산

from typing import List

def solution(n: int)->int:
    count = 0
    
    coin_types = [500, 100, 50, 10]
    for coin in coin_types:
        count += n // coin
        n %= coin

    return count

print(solution(1260))