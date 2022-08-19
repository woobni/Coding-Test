n, m=map(int, input().split())

answer=0
price_list=[]
for _ in range(m):
    price=list(map(int, input().split()))
    price_list.append(price)

six_string_list=sorted(price_list, key=lambda x: x[0])
one_string_list=sorted(price_list, key=lambda x: x[1])

# print(six_string_list)
# print(one_string_list)

if six_string_list[0][0] <= one_string_list[0][1] * 6:
    answer=six_string_list[0][0] * (n // 6) + one_string_list[0][1] * (n % 6)
    if six_string_list[0][0] < one_string_list[0][1] * (n % 6):
        answer=six_string_list[0][0] * (n // 6 + 1)
else:
    answer=one_string_list[0][1] * n

print(answer)