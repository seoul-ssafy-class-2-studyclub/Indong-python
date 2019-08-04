import sys
sys.stdin = open('input.txt', 'r')

cdn =  [(-1, 0), (-1, 1), (0, 1), (1, 1), 
    (1, 0), (1, -1), (0, -1), (-1, -1)]
                
case_size = int(input())
for case in range(1, case_size + 1):
    N = int(input())
    matrix = []
    count = 0
    for row in range(N):
        matrix.append([char for char in input()])

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '.':
                matrix[i][j] = 0
            elif matrix[i][j] == '*':
                for idx in range(8):
                    xi = i + cdn[idx][0]
                    yi = j + cdn[idx][1]
                    if 0 <= xi < N and 0 <= yi < N and matrix[xi][yi] != '*':
                        matrix[xi][yi] = 1

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                count += 1
                q = []
                q.append(i)
                q.append(j)
                matrix[i][j] = -1
                while q:
                    n = q.pop(0)
                    m = q.pop(0)
                    for idx in range(8):
                        ni = n + cdn[idx][0]
                        mi = m + cdn[idx][1]
                        if 0 <= ni < N and 0 <= mi < N:
                            if matrix[ni][mi] == 0:
                                q.append(ni)
                                q.append(mi)
                            matrix[ni][mi] = -2

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '*':
                continue
            elif matrix[i][j] > 0:
                count += 1

    print(f'#{case} {count}')
