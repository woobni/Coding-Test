import heapq 

n = int(input())
cardList = []
for i in range(n):
    card = int(input())
    heapq.heappush(cardList, card)

answer=0
while len(cardList) != 1:
    num1 = heapq.heappop(cardList)
    num2 = heapq.heappop(cardList)
    sum_value = num1 + num2
    answer += sum_value
    heapq.heappush(cardList, sum_value)

print(answer)