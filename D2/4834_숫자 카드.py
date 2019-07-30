case_size = int(input())
for case in range(1, case_size + 1):
    N = int(input())
    cards = [int(i) for i in input()]
    count = [0] * 10

    for i in range(0, N):
        count[cards[i]] += 1

    number = 0
    result = 0
    for i in range(len(count)):
        if count[i] >= result:
            result = count[i]
            number = i

    print(f'#{case} {number} {result}')
    