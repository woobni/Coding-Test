from typing import List

def solution(n: int)->int:
    count = 0
    
    coin_types = [500, 100, 50, 10]
    for coin in coin_types:
        count += n // coin
        n %= coin

    return count

print(solution(1260))