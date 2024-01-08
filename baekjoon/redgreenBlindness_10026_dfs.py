# 적록색약인 경우 G를 R로 치환

from typing import List
import sys

sys.setrecursionlimit(10**5)
input=sys.stdin.readline

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

d = [(0,1), (0, -1), (1,0), (-1,0)]

def dfs(x, y):
    visited[x][y] = True
    color = graph[x][y]
    for dx, dy in d:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == color:
            dfs(nx, ny)
            
cnt, cnt2 = 0, 0

for y in range(N):
    for x in range(N):
        if visited[x][y] == False:
            dfs(x,y)
            cnt += 1

for y in range(N):
    for x in range(N):
        if graph[x][y] == 'G':
            graph[x][y] = 'R'
visited = [[False] * N for _ in range(N)]

for y in range(N):
    for x in range(N):
        if visited[x][y] == False:
            dfs(x,y)
            cnt2 += 1

print(cnt, cnt2)

'''
import sys
from collections import deque

def bfs(i, j, graph, area):
    queue = deque()
    queue.append((i, j))
    color = graph[i][j]
    visited[i][j] = area

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if color == graph[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = area
                    queue.append((nx, ny))


N = int(sys.stdin.readline())
arr = [sys.stdin.readline().strip() for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0 for _ in range(N)] for _ in range(N)]
area = 1
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, arr, area)
            area += 1

not_color_blindness_area = 0
for i in range(N):
    not_color_blindness_area = max(not_color_blindness_area, max(visited[i]))


visited = [[0 for _ in range(N)] for _ in range(N)]
area = 1
for i in range(N):
    arr[i] = arr[i].replace('R', 'G')
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, arr, area)
            area += 1

color_blindness_area = 0
for i in range(N):
    color_blindness_area = max(color_blindness_area, max(visited[i]))

print(not_color_blindness_area, color_blindness_area)
'''