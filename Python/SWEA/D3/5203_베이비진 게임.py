for case in range(1, int(input()) + 1):
    chk1 = [0] * 10
    chk2 = [0] * 10
    cards = list(map(int, input().split()))
    res = 0
    for i in range(0, 12, 2):
        bg_1 = False
        bg_2 = False
        a, b = cards[i], cards[i+1]
        chk1[a] += 1
        if chk1[a] >= 3:
            bg_1 = True
        if not bg_1:
            for j in range(a - 2, a + 1):
                if j < 0 or j > 7:
                    continue
                if chk1[j] and chk1[j+1] and chk1[j+2]:
                    bg_1 = True
                    break
        if bg_1:
            res = 1
            break

        chk2[b] += 1
        if chk2[b] >= 3:
            bg_2 = True
        if not bg_2:
            for j in range(b - 2, b + 1):
                if j < 0 or j > 7:
                    continue
                if chk2[j] and chk2[j+1] and chk2[j+2]:
                    bg_2 = True
                    break

        if bg_2:
            res = 2
            break

    print(f'#{case} {res}')
