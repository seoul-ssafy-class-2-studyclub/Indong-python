oper = ['+', '-', '*', '/']
for case in range(1, int(input()) + 1):
    code = list(input().split())
    stack = []
    result = 0
    for i in code:
        if i.isdigit():
            stack.append(int(i))
        elif i in oper:
            if len(stack) < 2:
                result = 'error'
                break
            a = stack.pop()
            b = stack.pop()
            if i == '+':
                stack.append(b + a)
            elif i == '-':
                stack.append(b - a)
            elif i == '*':
                stack.append(b * a)
            elif i == '/':
                if a == 0:
                    stack.append(b)
                else:
                    stack.append(b // a)
        elif i == '.':
            if len(stack) > 1:
                result = 'error'
            else:
                result = stack.pop()
                
    print(f'#{case} {result}')
