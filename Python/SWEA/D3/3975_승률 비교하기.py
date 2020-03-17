import math

result_list = [None]
case_size = int(input())
for case in range(case_size):
    A, B, C, D = map(int, input().split())
    Alice = A / B
    Bob = C / D
    if math.isclose(Alice, Bob):
        result_list.append('DRAW')
    elif Alice > Bob:
        result_list.append('ALICE')
    else:
        result_list.append('BOB')

for i in range(1, case_size + 1):
    print(f'#{i} {result_list[i]}')
