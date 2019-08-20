for case in range(1, 11):
    N = int(input())
    password = list(input().split())
    M = int(input())
    change = list(input().split())
    while change:
        idx = int(change[1])
        num = int(change[2])
        for i in range(num):
            password.insert(idx + i, change.pop(3))
        del change[0:3]
    result = ' '.join(password[0:10])
    print(f'#{case} {result}')
