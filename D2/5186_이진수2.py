for case in range(1, int(input()) + 1):
    N = float(input())
    i = 1
    bin_num = ''
    is_over = True
    while i < 13:
        div = 2 ** -i
        if N >= div:
            N -= div
            bin_num += '1'
        else:
            bin_num += '0'
        i += 1
        if N == 0:
            is_over = False
            break
    
    if is_over:
        print(f'#{case} overflow')
    else:
        print(f'#{case} {bin_num}')
