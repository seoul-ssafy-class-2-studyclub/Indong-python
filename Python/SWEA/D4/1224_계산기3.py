def postfix(expr):
    isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
 
    stack = []
    calc = []
    top = ''
 
    for i in expr:
        if i.isdigit():
            calc.append(i)
        elif not stack:
            stack.append(i)
        elif i == ')':
            while True:
                temp = stack.pop()
                if temp == '(':
                    break
                calc.append(temp)
        elif isp[top] < icp[i]:
            stack.append(i)
        elif isp[top] >= icp[i]:
            while isp[top] >= icp[i]:
                calc.append(stack.pop())
                top = stack[-1]
            stack.append(i)
        if stack:
            top = stack[-1]
 
    return calc
 
def cal(code):
    oper = ['+', '-', '*', '/']
    stack = []
    for i in code:
        if i.isdigit():
            stack.append(int(i))
        elif i in oper:
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
    return stack[0]
 
for case in range(1, 11):
    N = int(input())
    expr = input()
    print(f'#{case} {cal(postfix(expr))}')
