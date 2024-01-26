from collections import deque

n = int(input())

def bfs(x,y,tx,ty):
    graph[x][y] = 1
    steps = [(-2, -1), (-1, -2), (1, -2), (-2, 1), (1, 2), (2, 1), (-1, 2), (2, -1)]
    q = deque()
    q.append((x, y))
    while q :
        x, y = q.popleft()
        if x == tx and y == ty :
            return graph[x][y] - 1 
        
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]
            if 0<=nx<l and 0<=ny<l and graph[nx][ny] == 0 :
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

for _ in range(n) :
    l = int(input())
    # 현재 나이트의 위치 입력 받기
    x, y = map(int, input().split())
    # 목표
    tx, ty = map(int, input().split())
    graph = [[0]*l for _ in range(l)]

    print(bfs(x,y,tx,ty))