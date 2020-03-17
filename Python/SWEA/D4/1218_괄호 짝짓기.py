left = ['(', '[', '{', '<']
right = [')', ']', '}', '>']

# string_list = ['{', '[', '(', ')', ']', '}', '<', '>', '[', '<', '{', '}', '>', '<', '>', ']']
for case in range(1, 11):
    N = int(input())
    string_list = list(input())
    stack = []
    result = 1
    for char in string_list:
        if char in left:
            stack.append(char)
        elif char in right:
            if left.index(stack.pop()) != right.index(char):
                result = 0
                break
    if stack:
        result = 0

    print(f'#{case} {result}')
