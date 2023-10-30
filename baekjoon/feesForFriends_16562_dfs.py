import sys
sys.setrecursionlimit(10**9)

# 학생 수 N (1 ≤ N ≤ 10,000), 친구관계 수 M (0 ≤ M ≤ 10,000), 가지고 있는 돈 k (1 ≤ k ≤ 10,000,000)
n,m,k = map(int, sys.stdin.readline().split())
money = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n)]

ans = []
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

visited = [False] * n

def dfs(x, g):
    visited[x] = True
    for i in graph[x]:
        if visited[i] == False:
            g.append(i)
            dfs(i, g)
    return g

for i in range(n):
    if visited[i] == False : # 정점 i가 False라면 다른 그룹에 있음 -> dfs
        group = dfs(i, [i])
        min_money = 10000000
        for j in group:
            if min_money > money[j]:
                min_money = money[j]
        ans.append(min_money)

if sum(ans) <= k:
    print(sum(ans))
else:
    print('Oh no')