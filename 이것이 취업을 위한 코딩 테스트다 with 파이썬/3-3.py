# key point
# 각 행을 입력 받음과 동시에 가장 작은 수를 업데이트

# Input N, M seperated by space.
n, m = map(int, input().split())

result = 0
# Input one line at a time and check.
for i in range(n):
    data = list(map(int, input().split()))
    # Find the smallest number in the current line.
    min_value = min(data)
    # Find the largest number in the smallest numbers.
    result = max(result, min_value)

print(result)
