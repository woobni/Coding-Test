from typing import List

# 이진 탐색(반복문) 알고리즘
def binary_search(arr: List[int], target: int, start: int, end: int) -> bool:
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if arr[mid] == target:
            return mid

        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif arr[mid] > target:
            end = mid - 1
        
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# 가지고 있는 숫자 카드 개수 입력받기
n = int(input())
# 숫자 카드 입력받기
card_arr = list(map(int, input().split(' ')))

# 찾을 정수 개수 입력받기
m = int(input())
# 찾을 정수 입력받기
num_arr = list(map(int, input().split(' ')))

# 이진 탐색을 수행하기 위해 정렬
card_arr.sort()

# 정수가 있는지 하나씩 확인
for target in num_arr:
    result = binary_search(card_arr, target, 0, n-1) # 끝의 인덱스는 n-1
    if result != None:
        print('1', end=' ')
    else:
        print('0', end=' ')