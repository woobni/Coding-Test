# m개의 지역에 n개의 다리를 놓을 수 있는 경우의 수를 구하는 것
# mCn 으로 표현할 수 있고 이는 m! 을 n!(m-n)! 으로 나눈 값
# 테스트 케이스마다 팩토리얼을 구하게 되면 매번 연산을 해야 되므로 시간이 오래 걸리는데, 
# 숫자의 범위가 30까지이므로 30까지의 팩토리얼을 미리 구해 놓은 뒤 이용하게 되면 좀 더 빠르게 해결

factorial = [1] * 31
for i in range(2, 31):
    factorial[i] = factorial[i-1] * i

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    bridge = factorial[m] // (factorial[n] * factorial[m-n])
    print(bridge)

# DP
dp = [[1] * 31 for _ in range(31)]
for i in range(31):
    dp[1][i] = i
for i in range(2, 31):
    for j in range(i + 1, 31):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(dp[n][m])