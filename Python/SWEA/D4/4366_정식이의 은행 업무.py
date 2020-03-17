for case in range(1, int(input()) + 1):
    bin_num = list(map(int, input()))
    tri_num = list(map(int, input()))
    chk = []
    N = len(bin_num)
    M = len(tri_num)
    money = 0
    for i in range(N):
        bi = bin_num[:]
        if bi[i]:
            bi[i] = 0
        else:
            bi[i] = 1
        bin_rec = sum([2 ** j * bi[-1-j] for j in range(N)])
        chk.append(bin_rec)

    for j in range(M):
        tri = tri_num[:]
        cand = [0, 1, 2]
        cand.remove(tri[j])
        for c in cand:
            tri[j] = c
            tri_rec = sum([3 ** k * tri[-1-k] for k in range(M)])
            if tri_rec in chk:
                money = tri_rec
        if money:
            break
    print(f'#{case} {money}')
