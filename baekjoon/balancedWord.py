while True :
    sentence = input()
    stack = []

    if sentence == "." :
        break

    for i in sentence :
        # 여는 괄호는 스택에 추가
        if i == '[' or i == '(' :
            stack.append(i)

        # 닫는 괄호가 스택 맨위의 여는 괄호랑 일치하면 스택에서 지워주기
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() 
            else : 
                stack.append(']')
                break
        
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break

    if len(stack) == 0 :
        print('yes')
    else :
        print('no')