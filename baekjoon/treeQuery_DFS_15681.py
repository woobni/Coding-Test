from typing import List
import sys

# 자기 호출 개수 제한. 안하면 메모리 초과..ㅂㄷ 아래 옵션으로 늘려줘야 함
# Python3의 기본 재귀 깊이가 1000이므로 재귀깊이를 해제한다
sys.setrecursionlimit(10**6)
# 안하면 시간 초과..ㅂㄷ
input=sys.stdin.readline

# 트리의 정점의 수 N과 루트의 번호 R, 쿼리의 수 Q
N, R, Q = map(int, input().split())
# 2차원 리스트(인접 행렬)
graph = [[] for _ in range(N+1)] # 1부터 시작하므로 n+1
# 노드의 부모를 기록하는 리스트
visited = [0] * (N+1)

# 트리에 속한 간선의 정보
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 노드의 부모를 기록하는 리스트
visited = [0] * (N+1)

def dfs(graph: List[int], vertex: int, visited: List[int]):
    visited[vertex] = 1
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[vertex]:
        if not visited[i]: 
            dfs(graph, i, visited)
            # 각 노드에 대한 서브 트리의 수를 저장
            visited[vertex] += visited[i]

dfs(graph, R, visited)

for i in range(Q):
    q = int(input())
    print(visited[q])