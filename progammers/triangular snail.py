from typing import List

def solution(n: int) -> List[int]:
    answer = []

    # 삼각형 만들기
    arr = []
    for i in range(1, n+1):
        arr.append([0] * i)

    # 시작 좌표
    x, y = -1, 0 # 아래부터 내려가므로
    val = 1

    # 하-우-상 방향순으로 이차원 리스트에 값 채워넣기
    for i in range(n): # 방향(하, 우, 상)
        for _ in range(i, n):
            if i % 3 == 0: # 하
                x += 1
                arr[x][y] = val
            
            elif i % 3 == 1: # 우
                y += 1
                arr[x][y] = val
            
            else: # 상
                x -= 1
                y -= 1
                arr[x][y] = val

            val += 1

    for element in arr:
        answer += element

    return answer

print(solution(4))
print(solution(5))
print(solution(6))