for case in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    chk_homework = [True] + [False] * N
    good_students = list(map(int, input().split()))
    for i in good_students:
        chk_homework[i] = True
    result = [i for i in range(N + 1) if chk_homework[i] == False]
    result.sort()
    print(f'#{case} {" ".join(map(str, result))}')
