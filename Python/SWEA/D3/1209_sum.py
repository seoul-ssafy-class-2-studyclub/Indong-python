for case in range(1, 11):
    N = int(input())
    matrix = []
    result = 0
    for i in range(100):
        row = list(map(int, input().split()))
        temp_sum = sum(row)
        if temp_sum > result:
            result = temp_sum
        matrix.append(row)
    for j in range(100):
        temp_sum = sum([matrix[k][j] for k in range(100)])
        if temp_sum > result:
            result = temp_sum
    temp_sum = sum([matrix[l][l] for l in range(100)])
    temp_sum_b = sum([matrix[l][-1-l] for l in range(100)])
    if temp_sum > result:
        result = temp_sum
    elif temp_sum_b > result:
        result = temp_sum_b
    
    print(f'#{N} {result}')
