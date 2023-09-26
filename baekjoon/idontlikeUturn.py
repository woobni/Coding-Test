# 막다른 곳은 인접한 길이 1개 또는 0개. 막다른 길이 아니기 위해서는 인접한 길이 적어도 2개 이상이어야 함
import sys
input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

def has_uturn(x, y):
    cnt = 0
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.':
            cnt += 1
    return cnt <= 1

found_uturn = any(graph[x][y] == '.' and has_uturn(x, y) for x in range(n) for y in range(m))

if found_uturn:
    print(1)
else:
    print(0)