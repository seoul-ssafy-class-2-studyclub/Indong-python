case_size = int(input())
for case in range(case_size):
    D, A, B, F = map(int, input().split())
    time = D / (A + B)
    result = F * time
    print(f'#{case + 1} {result:.6f}')