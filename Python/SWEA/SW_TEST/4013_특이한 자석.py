def rotate(num, di):
    global gears
    num_l = num
    num_r = num
    left = num - 1
    right = num + 1
    dl = di * -1
    dr = di * -1
    chk = [0, 0, 0, 0]
    chk[num] = di
    while 0 <= left:
        if gears[left][2] == gears[num_l][6]:
            break
        chk[left] = dl
        dl = dl * -1
        num_l = left
        left -= 1
    while right < 4:
        if gears[num_r][2] == gears[right][6]:
            break
        chk[right] = dr
        dr = dr * -1
        num_r = right
        right += 1
    for i in range(4):
        if chk[i] == 1:
            gears[i] = gears[i][7:] + gears[i][0:7]
        elif chk[i] == -1:
            gears[i] = gears[i][1:] + gears[i][:1]


for case in range(1, int(input()) + 1):
    K = int(input())
    gears = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K):
        num, di = map(int, input().split())
        rotate(num-1, di)

    ans = 0
    for i in range(4):
        if gears[i][0]:
            ans += (2 ** i)

    print(f'#{case} {ans}')
