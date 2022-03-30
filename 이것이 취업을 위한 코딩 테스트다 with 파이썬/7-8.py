# 문제 범위가 너무 크다(10억) -> 이진 탐색?

# 잘랐을 때의 떡의 양 계산하는 함수
def cutting(arr, h, n):
    total = 0
    for i in range(n):
        if arr[i] > h:
            total += arr[i] - h
    return total

# def cutting(arr, h):
#     for i in range(len(arr)):
#         temp = arr[i]- h
#         if temp < 0:
#             arr[i] = 0
#         else:
#             arr[i] = temp
#     return sum(arr)

# 떡의 개수 N, 요청한 떡의 길이 M 입력받기
n, m = map(int, input().split(' '))
# 개별 떡의 높이
arr = list(map(int, input().split(' ')))

start = 0
end = max(arr)
h_list = []
while start <= end :
    h = ( start + end ) // 2

    # 요청한 떡의 길이보다 작은 경우 왼쪽 확인
    if cutting(arr, h) < m :
        end = h - 1

    # 요청한 떡의 길이보다 충분한 경우 오른쪽 확인
    else : # cutting(arr, h) >= m
        h_list.append(h) # 최소한 m이 나오면 되고 최대의 h를 구해야 하므로
        start = h + 1

print(h_list)
print(max(h_list))