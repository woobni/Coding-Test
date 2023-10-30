# <, > 안에 있는 문자열은 그대로 출력하고, 그 밖에 있는 문자들을 스택에 담는다. 공백이 있을 경우 스택에 담았던 문자열을 뒤집어 출력한다.
# 연속하는 두 단어는 공백 하나로 구분함 -> 공백이 나오면 현재 스택에 있는 건 단어

ans = ""
tag = False
stack = ""
for i in input():
    if i == "<":
        tag = True
        ans += stack[::-1]
        stack = ""
        ans += i
        continue
    elif i == ">":
        tag = False
        ans += i
        continue
    elif i == " ":
        ans += stack[::-1] + " "
        stack = ""
        continue
        
    if tag:
        ans += i
    else:
        stack += i
print(ans+stack[::-1])