money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

case_size = int(input())
for case in range(1, case_size + 1):   
    money_dict = {50000: 0,
    10000: 0,
    5000: 0,
    1000: 0,
    500: 0,
    100: 0,
    50: 0,
    10: 0}
    N = int(input())
    M = 0
    i = 0
    while M != N and i < len(money_list):
        if N > M:
            M += money_list[i]
            money_dict[money_list[i]] += 1
        elif N < M:
            M -= money_list[i]
            money_dict[money_list[i]] -= 1
            i += 1
    print(f'#{case}')

    for value in money_dict.values():
        print(value, end=' ')
    print()
