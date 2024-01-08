import sys

N = int(input())
stack = []
cnt = 1 # 번호표 순서로만 간식을 줄 수 있음 -> 1부터 시작
numbers = list(map(int, sys.stdin.readline().split()))
while numbers:
    if cnt==numbers[0]:
        cnt+=1
        numbers.pop(0)
    else:
        stack.append(numbers.pop(0))

    while stack:
        if stack[-1] == cnt:
            stack.pop()
            cnt+=1
        else:
            break

if len(stack)==0:
    print("Nice")
else:
    print("Sad")