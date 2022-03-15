# 공간의 크기 N을 입력 받기
n = int(input())
x, y = 1, 1
# 이동 계획을 입력 받기
plans = input().split()

# L, R, U, D에 따른 이동 방향(그림 예시를 보고 파악)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            ax = x + dx[i] 
            ay = y + dy[i]

    # 공간을 벗어나는 경우 무시
    if ax < 1 or ay < 1 or ax > n or ay > n:
        continue
    # 이동 수행
    x, y = ax, ay

print(x,y)