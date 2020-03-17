for case in range(1, int(input()) + 1):
    num = input()
    chk_odd = int(num[-1])
    if chk_odd % 2 == 1:
        print(f'#{case} Odd')
    else:
        print(f'#{case} Even')
