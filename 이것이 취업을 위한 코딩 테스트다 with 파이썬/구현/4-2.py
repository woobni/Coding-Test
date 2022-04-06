# key point 
# 단순히 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지 확인
# 하루의 모든 경우의 수는 86,400초 
# 완전 탐색(brute forcing) -> 확인해야 할 전체 데이터 개수가 100만개 이하일 때 사용

# H를 입력 받기
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 3이 포함되어 있으면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)