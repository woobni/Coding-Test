# key point
# 주어진 수에 대하여 최대한 많이 나누면 될 거라 생각
# 2 이상의 수로 나누는 게 1을 빼는 것 보다는 숫자를 훨씬 많이 줄일 수 있을 것이기 때문

n, k = map(int, input().split())
result = 0

# If n>k, then keep dividing by k.
while n >= k:
    # If n cannot be divided by k, then subtract 1 from n.
    while n%k != 0:
        n -= 1
        result += 1
    # divide by k
    n //= k
    result += 1

# Subtract 1 until it becomes 1.
while n > 1:
    n -= 1
    result += 1

print(result)
    
