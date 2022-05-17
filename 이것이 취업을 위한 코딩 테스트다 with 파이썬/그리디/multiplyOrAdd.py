info = input() # 여기서 int로 변환시키면 슬라이싱 못함
answer = int(info[0])

# 두 수 중에서 하나라도 1이하인 경우에는 더하고 두 수가 모두 2이상인 경우에는 곱하자
for i in range(1, len(info)):
    num = int(info[i])
    if num <= 1 or answer <= 1:
        answer += num
    else:
        answer *= num

print(answer)