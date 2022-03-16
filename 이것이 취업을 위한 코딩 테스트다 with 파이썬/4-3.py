# 현재 나이트의 위치 입력 받기
info = input()
x = int(info[1])
y = int(ord(info[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향
steps = [(-2, -1), (-1, -2), (1, -2), (-2, 1), (1, 2), (2, 1), (-1, 2), (2, -1)]

# 8가지 방향에 대해 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    nx = x + step[0]
    ny = y + step[1]

    # 해당 위치로 이동 가능하면 카운트 증가
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        result += 1

print(result)