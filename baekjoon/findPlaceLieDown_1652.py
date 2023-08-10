# 연속으로 . 있는 걸 찾기
import sys

input = sys.stdin.readline

N = int(input())

graph = [input().strip() for _ in range(N)]

row_cnt, col_cnt = 0, 0
for i in range(N):
    tmp_row_cnt, tmp_col_cnt = 0, 0
    for j in range(N):
        if graph[i][j] == '.':
            tmp_row_cnt += 1

        else :
            if tmp_row_cnt > 1:
                row_cnt += 1
            tmp_row_cnt = 0

        if graph[j][i] == '.':
            tmp_col_cnt += 1
        else :
            if tmp_col_cnt > 1:
                col_cnt += 1
            tmp_col_cnt = 0
            
    if tmp_row_cnt > 1:
        row_cnt += 1

    if tmp_col_cnt > 1:
        col_cnt += 1
            
print(row_cnt, col_cnt)