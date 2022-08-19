import sys
from collections import deque

input = sys.stdin.readline
# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X 입력받기
n, m, k, x = map(int, input().split())
# 인접 리스트 생성
graph = [[] for _ in range(n+1)] # 인덱스 0 버리고 1부터 시작

# 두 도시를 연결하는 도로 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 출발 도시에서부터의 최단 거리 초기화
distance = [-1] * (n+1)


def bfs(graph, start, distance):
    queue = deque([start])
    distance[x] = 0 # 출발 도시까지의 거리는 0

    while queue:
        now = queue.popleft()
        # 현재 도시에서 방문할 수 있는 모든 도시를 확인
        for next in graph[now]:
            # 아직 방문하지 않았다면
            if distance[next] == -1:
                queue.append(next)
                # 최단 거리 갱신
                distance[next] = distance[now] + 1

bfs(graph, x, distance)

# 최단 거리가 K인 도시 출력
check = False
for i in range(1, n+1):
    if distance[i]==k:
        print(i)
        check = True

# K인 도시가 없으면 -1 출력
if check==False:
    print(-1)