# bfs -> queue

# deque - 내부적으로 deque은 double-linked list로 구현되어 있음. 그래서 양 끝의 요소의 추가/삭제가 O(1)을 만족하게 됨
# <-> 리스트 - 리스트의 마지막 원소를 삭제는 O(1)이지만, 첫번째 원소를 삭제하면 삭제 후 모든 원소를 앞으로 이동시키기 때문에 시간 복잡도가 O(n)
from collections import deque

# M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

def bfs():
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

bfs()

anw = 0
for row in graph:
    for j in row:
        if j == 0:
            print(-1)
            exit(0)
    anw = max(anw, max(row))

print(anw - 1) # 처음 시작을 1로 했으니 -1