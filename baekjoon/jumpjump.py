# DP
import sys
input = sys.stdin.readline

# 미로의 크기(가로) n 입력받기
n = int(input())
# 미로 입력받기
miro = list(map(int, input().split()))

dp = [n+1] * n # min() 계산해야 하므로 나올 수 없는 큰 값인 n+1로 초기화
dp[0] = 0
for i in range(n):
    for j in range(1, miro[i]+1):
        if i+j >= n:
            break
        dp[i+j] = min(dp[i+j], dp[i]+1)
print(dp[n-1] if dp[n-1] != n+1 else -1)


# BFS
n = int(input())
miro = list(map(int, input().split()))

visited = [-1] * n

def bfs(start):
    q = []
    q.append(start)
    visited[start] = 0
    while q:
        now = q.pop(0)
        jump = miro[now]
        for i in range(jump, 0, -1): # range(0, jump+1)
            if now + i < n and visited[now + i] == -1:
                visited[now + i] = visited[now] + 1
                q.append(now + i)

bfs(0)
print(visited[-1])