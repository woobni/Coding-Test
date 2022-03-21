# N, M을 공백으로 구분해서 입력 받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

# 현재 캐릭터의 x좌표, y좌표, 방향(0,1,2,3) 입력 받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리. 좌표는 (0,0)부터 존재

# 전체 맵 정보 입력 받기
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 가로 x축, 세로 y축 일 때
# 북, 동, 남, 서 방향 정의  
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1 # 북0 동1 남2 서3
    if direction == -1:
        direction = 3 # 왼쪽으로 이동할 방향(서)

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있다면 이동하기
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)
