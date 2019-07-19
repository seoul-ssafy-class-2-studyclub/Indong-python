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


case_size = int(input())
try:
    for case in range(case_size):
        size, kf = map(int, input().split())
        matrix = []
        if (5 <= size <= 15) and (2 <= kf <= size):
            for row in range(size):
                horizontal_list = list(map(int, input().split()))
                if list(filter(lambda x: x > 30, horizontal_list)) or len(horizontal_list) != size:
                    raise ValueError
                else:
                    matrix += [horizontal_list]
        else:
            raise ValueError
        result = dead_fly(matrix, size, kf)
        print("#{0} {1}".format(case + 1, result))
except ValueError:
    print('올바른 범위의 수를 입력해주세요.')