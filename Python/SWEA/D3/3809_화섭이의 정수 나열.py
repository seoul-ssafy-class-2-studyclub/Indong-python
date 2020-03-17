for case in range(1, int(input()) + 1):
    N = int(input())
    num_list = []
    while len(num_list) < N:
        num_list += list(input().split())
    chk = ''.join(num_list)

    result = 0
    while True:
        if str(result) not in chk:
            break
        result += 1
        
    print(f'#{case} {result}')