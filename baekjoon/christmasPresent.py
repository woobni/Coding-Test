import heapq 
import sys
input = sys.stdin.readline

n = int(input())
gifts = []

for i in range(n):
    a = list(map(int, input().split()))
    if a[0]==0:
        if len(gifts)==0:
            print(-1)
        else:
            tmp = -heapq.heappop(gifts)
            print(tmp)
    else:
        for j in range(a[0]):
            heapq.heappush(gifts, -a[j+1])