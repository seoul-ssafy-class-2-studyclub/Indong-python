for case in range(1, int(input()) + 1):
    word = list(input())
    stack = []
    for char in word:
        if not stack or stack[-1] != char:
            stack.append(char)
        else:
            stack.pop()
    print(f'#{case} {len(stack)}')
