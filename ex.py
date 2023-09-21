n,kim,rim=map(int, input().split())
cnt=0
while kim != rim:
  kim -= kim // 2
  rim -= rim // 2
  cnt += 1
print(cnt)