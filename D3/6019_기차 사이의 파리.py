case_size = int(input())
try:
    for case in range(case_size):
        D, A, B, F = map(int, input().split())
        if 1 <= D <= (10 ** 3) and 1 <= A <= B < F < (10 ** 2) :
            time = D / (A + B)
            result = F * time
            print(f'#{case + 1} {result:.7f}')
        else:
            raise ValueError
except ValueError:
    print('올바른 범위의 수를 입력해주세요.')