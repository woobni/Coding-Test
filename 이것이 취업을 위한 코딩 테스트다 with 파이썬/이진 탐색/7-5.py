# 이진 탐색

# 이진 탐색 소스코드 구현(반복문)
def binary_search ( array , target , start , end ):
    while start <= end :
        mid = ( start + end ) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array [ mid ] == target :
            return mid

        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array [ mid ] > target :
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else :
            start = mid + 1
    return None

# 매장의 부품 개수 N 입력받기
n = int(input())
# 매장의 부품 종류 입렫받기
parts = list(map(int, input().split(' ')))
# 요청 받은 부품 개수 M 입력받기
m = int(input())
# 요청 받은 부품 종류 입렫받기
req_parts = list(map(int, input().split(' ')))

# 이진 탐색을 수행하기 위해 사전에 정렬 수행
parts.sort()

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in req_parts :
    # 해당 부품이 존재하는지 확인
    result = binary_search ( parts , i , 0 , n - 1 )
    if result != None :
        print (' yes ', end = ' ')
    else :
        print (' no ', end = ' ')