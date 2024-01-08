'''
https://www.acmicpc.net/problem/2458

자신이 갈 수 있는 노드들은 자기보다 작은 사람들이며 자신에게 오는 경로가 있는 노드들은 자기보다 큰 사람들이다.

이 둘의 합이 자신을 제외한 N-1인 경우 자신의 순서를 알 수 있는 것이다. (i노드에서 다른 노드들로 가는 값들과, 다른 노드들에서 i노드로 갈 수 있는 값을 모두 합 == N-1)
'''
import sys

N, M = map(int, input().split()) # 6 6
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    tall, small = map(int, sys.stdin.readline().split())
    graph[tall][small] = 1

# 플로이드 와샬 알고리즘
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] == 1 and graph[k][j] == 1: # i>k k>j
                graph[i][j] = 1 # j가 자신 i보다 작은 경우

answer = 0
for i in range(1, N+1):
    known_height = 0
    for j in range(1, N+1):
        known_height += graph[i][j] + graph[j][i] # 자신보다 작은 사람과 큰 사람의 합
    if known_height == N-1: # 자신의 키 순서를 알 경우
        answer += 1
print(answer)