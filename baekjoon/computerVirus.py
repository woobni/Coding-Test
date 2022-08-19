# 컴퓨터의 수(노드의 개수) 입력받기
n = int(input())
# 연결되어 있는 컴퓨터 쌍의 수(간선의 개수) 입력받기
m = int(input()) 
# 2차원 리스트(인접 행렬)
graph = [[] for _ in range(n + 1)] # 1부터 시작하므로 n+1

# 연결된 컴퓨터 쌍 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 노드가 방문한 정보를 기록하는 리스트
visited = [0] * (n + 1)

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = 1
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
# 방문한 노드수 - 노드1
print(sum(visited)-1)