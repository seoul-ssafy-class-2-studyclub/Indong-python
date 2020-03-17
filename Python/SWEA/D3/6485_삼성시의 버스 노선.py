case_size = int(input())
for case in range(1, case_size + 1):
    count_list = [0] * 5001
    N = int(input())
    for bus in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            count_list[i] += 1        
    P = int(input())
    result_list = [count_list[int(input())] for j in range(P)]
    print(f'#{case} {" ".join(map(str, result_list))}')
