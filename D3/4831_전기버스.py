import math
T = int(input())
list_result = []

try:
    if 1 <= T <= 50:
        for test_case in range(T):
            bus = 0
            count = 0
            K, N, M = list(map(int, input().split()))
            list_charge = list(map(int, input().split()))
            min_charge = math.floor(N/K)
            move = K
            if (1 <= K and N and M <= 100) and (len(list_charge) == M):
                while bus < N:
                    if bus + move == N:
                        break
                    elif (bus + move) in list_charge:
                        count += 1
                        bus += move
                        move = K
                    else:
                        move -= 1
                        if move == 0:
                            count = 0
                            break
                list_result += [count]
            else:
                raise ValueError
    else:
        raise ValueError

    for key, value in enumerate(list_result):
        print("#{0} {1}".format(key + 1, value))

except ValueError:
    print("올바른 숫자를 입력하세요.")
