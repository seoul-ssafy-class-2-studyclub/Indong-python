def rotation_matrix(board, N):
    array = []
    for i in range(N):
        vertical_list = [board[j][i] for j in range(N-1, -1, -1)]
        array += [vertical_list]
    return array


case_size = int(input())
for case in range(1, case_size + 1):
    matrix = []
    length = int(input())
    for numbers in range(length):
        matrix.append(list(map(int, input().split())))
    matrix_90 = rotation_matrix(matrix, length)
    matrix_180 = rotation_matrix(matrix_90, length)
    matrix_270 = rotation_matrix(matrix_180, length)
    print(f'#{case}')
    for j in range(length):
        row_90 = ''.join(map(str, matrix_90[j]))
        row_180 = ''.join(map(str, matrix_180[j]))
        row_270 = ''.join(map(str, matrix_270[j]))
        print(f'{row_90} {row_180} {row_270}')
        