# 숫자 카드 묶음 개수 N 입력받기
n = int(input())
# 카드 묶음의 크기 입력받기
cardList = []
for _ in range(n):
    cardList.append(int(input()))

# 작은 값부터 더해주기 위해 오름차순 정렬
cardList.sort()

if len(cardList)==1:
    print(0)
else:
    answer = cardList[0] + cardList[1]
    sum_counts = answer
    for i in range(2, n):
        sum_counts += cardList[i]
        answer += sum_counts

    print(answer)





# 우선순위 큐
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