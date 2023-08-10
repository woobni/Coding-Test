# knapsack[i][j] = max(현재 물건 가치 + knapsack[이전 물건][현재 가방 무게 - 현재 물건 무게], knapsack[이전 물건][현재 가방 무게])
# knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

import sys
input = sys.stdin.readline

# 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K
N, K = map(int,input().split())

items = [[0,0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    items.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = items[i][0] 
        value = items[i][1]
       
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] # weight보다 작으면 위의 값을 그대로 가져온다
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])