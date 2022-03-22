# 리스트를 하나는 오름차순, 하나는 내림차순 정렬. 첫 원소부터 바꿔치기  

# 원소의 수 N, 바꿔치기 횟수 K 입력받기
n, k = map(int, input().split(' '))
# 배열의 원소 입력받기
list_a = map(int, input().split(' '))
list_b = map(int, input().split(' '))

list_a = sorted(list_a)
list_b = sorted(list_b, reverse=True)

for i in range(k):
    if list_a[i] < list_b[i]:
        list_a[i], list_b[i] = list_b[i], list_a[i]

print(sum(list_a))