# 수열에 속해 있는 수의 개수
n = int(input())
# N개의 수 입력받기
input_list = []
for i in range(n):
    data = int(input())
    input_list.append(data)

# 리스트를 내림차순으로 정렬
input_list.sort(reverse=True)

print(input_list)