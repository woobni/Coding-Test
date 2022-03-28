# 데이터의 범위가 1,000,000 이하이기 때문에 계수 정렬을 사용 가능할 것 같음

# 매장의 부품 개수 N 입력받기
n = int(input())
# 매장의 부품 종류 입렫받기
parts = list(map(int, input().split(' ')))
# 요청 받은 부품 개수 M 입력받기
m = int(input())
# 요청 받은 부품 종류 입렫받기
req_parts = list(map(int, input().split(' ')))

# 모든 범위를 포함하는 리스트 선언(모든 값은 0 으로 초기화)
count = [0] * (max(parts) + 1)

for i in range(len(parts)):
	count[parts[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

result = []
for j in range(len(req_parts)):
    if count[req_parts[j]] == 1:
        result.append('yes')
    else:
        result.append('no')

print(result)