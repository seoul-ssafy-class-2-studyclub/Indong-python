from sys import stdin


def fill_sudoku(k=0):
    global flag
    if k >= N:
        flag = True
        return True
    y, x = blank[k]
    for i in range(1, 10):
        if not row[y][i] and not col[x][i] and not square[(y // 3) * 3 + (x // 3)][i]:
            row[y][i] = 1
            col[x][i] = 1
            square[(y // 3) * 3 + (x // 3)][i] = 1
            sudoku[y][x] = str(i)
            fill_sudoku(k+1)
            if flag:
                return True
            row[y][i] = 0
            col[x][i] = 0
            square[(y // 3) * 3 + (x // 3)][i] = 0
            sudoku[y][x] = '0'
    

row = [[0] * 10 for _ in range(9)]
col = [[0] * 10 for _ in range(9)]
square = [[0] * 10 for _ in range(9)]
sudoku = [list(stdin.readline().split()) for _ in range(9)]
blank = []
flag = False
for r in range(9):
    for c in range(9):
        num = int(sudoku[r][c])
        if num == 0:
            blank.append((r, c))
        else:
            row[r][num] = 1
            col[c][num] = 1
            square[(r // 3) * 3 + (c // 3)][num] = 1
N = len(blank)

fill_sudoku()
for i in range(9):
    print(' '.join(sudoku[i]))
