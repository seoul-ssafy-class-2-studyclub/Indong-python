left = ['(', '{']
right = [')', '}']

for case in range(1, int(input()) + 1):
    code = list(input())
    stack = []
    result = 1
    for char in code:
        if char in left:
            stack.append(char)
        elif char in right:
            if not stack or left.index(stack.pop()) != right.index(char):
                result = 0
                break
    if stack:
        result = 0
        
    print(f'#{case} {result}')
