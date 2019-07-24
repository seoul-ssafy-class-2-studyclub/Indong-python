def calc_total(middle, final, assignment):
    result = (middle * 0.35) + (final * 0.45) + (assignment * 0.2)
    return result

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
case_size = int(input())
for case in range(1, case_size + 1):
    N, K = map(int, input().split())
    score_list = []
    interval = int(N // 10)
    for student in range(N):
        mid, fin, homework = map(int, input().split())
        score_list.append(calc_total(mid, fin, homework))
    # K_score = score_list[K - 1]
    # score_list = sorted(score_list, reverse=True)    
    # k_index = score_list.index(K_score)
    # grade_index = int(k_index // interval)
    # print(f'{case} {grade[grade_index]}')

    score_list = enumerate(score_list)
    score_list = list(sorted(score_list, key=lambda x: x[1], reverse=True))

    for i in range(len(score_list)):
        if score_list[i][0] == K - 1:
            grade_index = int(i // interval)
            print(f'#{case} {grade[grade_index]}')
            