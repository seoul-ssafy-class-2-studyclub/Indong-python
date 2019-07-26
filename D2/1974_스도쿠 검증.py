# 7 3 6 4 2 9 5 8 1
# 5 8 9 1 6 7 3 2 4
# 2 1 4 5 8 3 6 9 7
# 8 4 7 9 3 6 1 5 2
# 1 5 3 8 4 2 9 7 6
# 9 6 2 7 5 1 8 4 3
# 4 2 1 3 9 8 7 6 5
# 3 9 5 6 7 4 2 1 8
# 6 7 8 2 1 5 4 3 9

def sudoku_check(s_list):
    sudoku_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    if sum(s_list) != 45:
        return False
    else:
        if set(s_list) != sudoku_set:
            return False
        else:
            return True


case_size = int(input())
for case in range(1, case_size + 1):
    switch = 1
    board = []
    for i in range(9):
        sudoku_list = list(map(int, input().split()))
        if sudoku_check(sudoku_list):
            board += [sudoku_list]
        else:
            switch = 0
    if switch == 1:
        for j in range(9):
            vertical_list = [board[k][j] for k in range(9)]
            if sudoku_check(vertical_list):
                continue
            else:
                switch = 0
                break
    if switch == 1:
        for l in range(0, 7, 3):
            for m in range(0, 7, 3):
                temp_list = []
                for row in range(3):
                    temp_list += board[m+row][l:l+3]
                if sudoku_check(temp_list):
                    continue
                else:
                    switch = 0
                    break
    if switch == 1:
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')
