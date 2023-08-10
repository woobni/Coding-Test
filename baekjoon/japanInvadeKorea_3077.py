import sys

input = sys.stdin.readline

n = int(input())

correct_answer = dict(zip(input().split(), [i for i in range(n)]))

to_check_answer = input().split()
cnt = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        if correct_answer[to_check_answer[i]] < correct_answer[to_check_answer[j]]:
            cnt += 1

print(cnt, "/", n * (n - 1) // 2, sep="")