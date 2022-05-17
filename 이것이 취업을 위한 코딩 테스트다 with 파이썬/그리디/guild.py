# 모험가의 수 n 입력받기
n = int(input())
# 각 모험가의 공포도 입력받기
fears = list(map(int, input().split()))

# 많은 수의 그룹이 나와야 되므로 오름차순으로 정렬해보자.
fears.sort()

answer = 0 # 총 그룹의 수
cnt = 0 # 현재 그룹의 모험가 수 
for fear in fears:
    cnt += 1 # 현재 그룹에 해당 모험가를 포함
    if cnt == fear:
        answer += 1
        cnt = 0

print(answer)
