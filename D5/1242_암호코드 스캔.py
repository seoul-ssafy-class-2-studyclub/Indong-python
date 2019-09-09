def chk_code(bi_num, mag=0):
    x = len(bi_num) - 1
    password = []
    while bi_num[x] == '0':
        x -= 1
    for i in range(8):
        ratio = [0, 0, 0, 0]
        while bi_num[x] != '0':
            ratio[3] += 1
            x -= 1
        while bi_num[x] == '0':
            ratio[2] += 1
            x -= 1
        while bi_num[x] != '0':
            ratio[1] += 1
            x -= 1
        if not mag:
            while bi_num[x] == '0':
                ratio[0] += 1
                x -= 1
            mag = sum(ratio) // 7
            # print(f'mag: {mag}')
            # print(ratio)
        else:
            ratio[0] += (7 * mag) - sum(ratio)
            x -= ratio[0]
        if mag > 1:
            ratio = map(lambda x: x // mag, ratio)
        password.insert(0, code[tuple(ratio)])
    return password

result_list = []
code = {(3, 2, 1, 1): 0, (2, 2, 2, 1): 1, (2, 1, 2, 2): 2, (1, 4, 1, 1): 3, (1, 1, 3, 2): 4,
(1, 2, 3, 1): 5, (1, 1, 1, 4): 6, (1, 3, 1, 2): 7, (1, 2, 1, 3): 8, (3, 1, 1, 2): 9}
for case in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    vis = [[False] * M for _ in range(N)]
    result = 0
    for c in range(M - 1, -1, -1):
        for r in range(N):
            if arr[r][c] != '0' and not vis[r][c]:
                # print((r, c))
                y, x = r, c
                # 나중에 방문 처리 하기 위해 맨 밑 지점의 y좌표를 구해놓는다.
                while arr[y+1][c] != '0':
                    y += 1
                corner = y

                temp = ''
                while x >= 0:
                    temp = format(int(arr[r][x], 16), '04b') + temp
                    x -= 1
                # print(temp)
                # print(len(temp))
                for j in range(r, y + 1):
                    for i in range(x + 1, c + 1):
                        vis[j][i] = True

                # 오른쪽에서부터 암호 확인.
                password = chk_code(temp)

                chk = 0
                for i in range(8):
                    if not i % 2:
                        chk += password[i] * 3
                    else:
                        chk += password[i]
                
                if not chk % 10:
                    result += sum(password)
    result_list.append(result)

for i in range(len(result_list)):
    print(f'#{i+1} {result_list[i]}')
