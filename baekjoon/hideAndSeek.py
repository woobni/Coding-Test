# 시작점이 5, 도착점 17
# 1초 : 4, 6, 10 (5-1, 5+1, 5*2)
# 2초 : 3, 7, 8, 9, 11, 12, 20 (수가 점점 많아진다)
# 3초 : ,.... 16,......,40 (생략)
# 4초 : 17,,,,32,,,(생략)

import sys
from collections import deque
input = sys.stdin.readline()

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break

        for j in (x-1,x+1,x*2):
            if 0<= j <= MAX and not dist[j]:
                dist[j] = dist[x] +1
                q.append(j)

MAX = 100000
n,k = map(int,input.split())
dist = [0] * (MAX+1)

bfs()