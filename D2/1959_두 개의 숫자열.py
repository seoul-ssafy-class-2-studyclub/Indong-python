case_size = int(input())
for case in range(case_size):
    N, M = map(int, input().split())
    list_N = list(map(int, input().split()))
    list_M = list(map(int, input().split()))
    result_list = []
    if N > M:
        list_N, list_M = list_M, list_N
        N, M = M, N
    for j in range(M - N + 1):  # i는 N의 인덱스, j는 M의 인덱스
        result_list += [sum([list_N[i] * list_M[i+j] for i in range(N)])]
        result = max(result_list)
    print(f'#{case + 1} {result}')    
