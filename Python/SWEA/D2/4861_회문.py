def manacher_pal(string, M):
    string = '#' + '#'.join(string) + '#'
    N = len(string)
    A = [0] * N
    r = 0
    p = 0
    for i in range(N):
        if i > r:
            A[i] = 0
        else:
            i_apo = (2 * p) - i
            if A[i_apo] >= r - i:
                A[i] = r - i
            else:
                A[i] = A[i_apo]
        while i - A[i] - 1 >= 0 and i + A[i] + 1 < N and string[i - A[i] - 1] == string[i + A[i] + 1]:
            A[i] += 1
        j = i + A[i]
        if j > r:
            r = j
            p = i
        
    for i in range(1, N, 2):
        if A[i] == 1:
            A[i] = 0
    
    idx = False
    for i in range(N):
        if A[i] == M:
            idx = i
            break
    if not idx:
        return idx

    result = ''
    for i in string[idx-M:idx+M+1]:
        if i == '#':
            continue
        result += i
    return result


for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = []
    result = ''
    for i in range(N):
        row = input()
        board.append(row)
        chk = manacher_pal(row, M)
        if chk:
            result = chk  
    if result:
        print(f'#{case} {result}')
        continue
    
    temp_str = ''
    for i in range(N):
        for j in range(N):
            temp_str += board[j][i]
        chk = manacher_pal(temp_str, M)
        if chk:
            print(f'#{case} {chk}')
            break
