row = [0, 0, 0, 0, 0]
col = [0, 0, 0, 0, 0]
dia = [0, 0]

bingo = []
for i in range(5):
    bingo.append(list(map(int, input().split())))

game = []
for i in range(5):
    game.extend(list(map(int, input().split())))

result = 0
cnt = 0
for n in range(25):
    if cnt >= 3:
        break
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == game[n]:
                row[i] += 1
                if row[i] == 5:
                    cnt += 1
                col[j] += 1
                if col[j] == 5:
                    cnt += 1
                if i == j:
                    dia[0] += 1
                    if dia[0] == 5:
                        cnt += 1
                if (i + j) == 4:
                    dia[1] += 1
                    if dia[1] == 5:
                        cnt += 1
                if cnt >= 3:
                    result = n + 1
                    break

print(result)
