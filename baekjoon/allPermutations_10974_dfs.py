'''
https://www.acmicpc.net/problem/10974
'''
def dfs(n, permutation):
    if len(permutation) == n:
        print(*permutation)
        return
    for i in range(1, n + 1): # [1 2 3] [1 3 2] [2 1 3] ... 
        if i not in permutation: 
            dfs(n, permutation + [i])

n = int(input()) # 3
dfs(n, [])