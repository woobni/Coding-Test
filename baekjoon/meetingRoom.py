# 회의 수 n 입력받기
n = int(input())
# 각 회의 시작 시간, 끝나는 시간 입력받기
times = []
for _ in range(n):
    times.append(list(map(int, input().split())))

times.sort(key=lambda x: x[0]) # 시작 시간 기준으로 정렬
times.sort(key=lambda x: x[1]) # 끝나는 시간 기준으로 정렬
# times.sort(key=lambda x: (x[1], x[0]))

cnt = 0
last = 0
for start, end in times:
    if start >= last:
        cnt += 1
        last = end

print(cnt)