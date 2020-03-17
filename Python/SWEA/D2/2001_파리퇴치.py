def dead_fly(mat, N, M):
    total_list = []
    # 전체 열 이동
    for k in range(N - M + 1):
        # 전체 행 이동
        for i in range(N - M + 1):
            total = 0
            # 파리채 크기 설정
            for j in range(M):
                total += sum(mat[k + j][i:i + M])
            total_list += [total]
    return max(total_list)


for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = dead_fly(board, N, M)
    print("#{0} {1}".format(case, result))
