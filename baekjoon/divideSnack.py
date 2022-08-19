import sys

# 조카의 수와 과자의 수 입력받기
m, n = map(int, sys.stdin.readline().split())
# 과자의 길이 공백으로 입력받기
snacks = list(map(int, sys.stdin.readline().split()))

# 특정 높이로 과자를 잘랐을 때 몇명에게 줄 수 있는지 확인하는 함수
def cutting(snacks, h):
    count = 0
    if h == 0:
        return count

    for snack in snacks:
        count += snack // h
    return count

start = 0
end = max(snacks)
h_list = []
while start <= end:
    h = ( start + end ) // 2

    if cutting(snacks, h) == 0:
        h_list.append(h)
        break

    # 조카수보다 과자가 부족한 경우 왼쪽 확인
    elif cutting(snacks, h) < m:
        end = h - 1

    # 조카수보다 과자가 충분한 경우 오른쪽 확인
    else : # cutting(arr, h) >= m
        h_list.append(h) # 최소한 m이 나오면 되고 최대의 h를 구해야 하므로
        start = h + 1

# print(h_list)
print(max(h_list))