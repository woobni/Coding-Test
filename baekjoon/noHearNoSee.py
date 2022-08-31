n, m = map(int, input().split())

no_hear = set()
no_see = set()
for i in range(n):
    no_hear.add(input())

for i in range(m):
    no_see.add(input())

answer = sorted(list(no_hear & no_see))

print(len(answer))
for i in answer:
    print(i)