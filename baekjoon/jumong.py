from typing import List

# 재료의 개수 n
n = int(input())
# 갑옷을 만드는데 필요한 수 m
m = int(input())
# 재료들의 고유 번호
nums = list(map(int, input().split()))

def twoSum(nums: List[int], target: int) -> int:
    cnt = 0
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1:]: # 현재 값을 버려가면서 나머지 리스트만 보기 때문에 중복이 나오지 않게 됨
            cnt += 1

    return cnt

print(twoSum(nums, m))