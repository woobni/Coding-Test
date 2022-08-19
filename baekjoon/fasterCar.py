import sys
input = sys.stdin.readline

# 차의 대수
n = int(input())

inCars = {}
outCars = []
cnt = 0

# 들어간 차를 딕셔너리로 받기
for i in range(n):
    inCars[input().rstrip("\n")] = i

# 나온 차를 리스트로 받기
for i in range(n):
    outCars.append(input().rstrip("\n"))

# 나온 i번째 차가 추월을 했는지 체크
for i in range(n-1): # 마지막 n번째 차는 추월한 차가 될 수 없음
    for j in range(i+1, n):
        if inCars[outCars[i]] > inCars[outCars[j]]:
            cnt += 1
            break
print(cnt)
