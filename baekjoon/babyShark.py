import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]

q = deque()
for row in range(n):
    tmp = list(map(int, input().split()))
    for col in range(m):
        if tmp[col] == 1:
            # 상어에서부터 거리를 계산해야 하므로 큐에 넣기
            q.append((row, col)) 
    arr.append(tmp)

def bfs():
    while q:
        x, y = q.popleft()
        for direction in range(len(dx)):
            nx, ny = x + dx[direction], y + dy[direction]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 0:
                q.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1

bfs()
dist = 0
for row in range(n):
    for col in range(m):
        dist = max(arr[row][col], dist)

print(dist - 1) # 거리에서 자기 자신 빼주기