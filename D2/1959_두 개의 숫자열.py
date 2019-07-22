case_size = int(input())
try:
    for case in range(case_size):
        N, M = map(int, input().split())
        if 3 <= (N and M) <= 20:
            list_N = list(map(int, input().split()))
            list_M = list(map(int, input().split()))
            result_list = []
            if N > M:
                list_N, list_M = list_M, list_N
                N, M = M, N
            for j in range(M - N + 1):
                result_list += [sum([list_N[i] * list_M[i+j] for i in range(N)])]
                result = max(result_list)
            print(f'#{case + 1} {result}')    
        else:
            raise ValueError

except ValueError:
    print('올바른 범위의 수를 입력해주세요.')
