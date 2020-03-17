def pal(word):
    N = len(word)
    for i in range(N // 2):
        if word[i] == '*' or word[-1-i] == '*':
            return True
        elif word[i] != word[-1-i]:
            return False
    return True


for case in range(1, int(input()) + 1):
    word = input()
    if pal(word):
        print(f'#{case} Exist')
    else:
        print(f'#{case} Not exist')
