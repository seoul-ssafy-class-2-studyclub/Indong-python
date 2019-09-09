def sudoku_check(sudoku):
    # 행 검색
    for r in range(9):
        chk = [False] * 10
        for c in range(9):
            num = sudoku[r][c]
            if chk[num]:
                return 0
            chk[num] = True

    # 열 검색        
    for c in range(9):
        chk = [False] * 10
        for r in range(9):
            num = sudoku[r][c]
            if chk[num]:
                return 0
            chk[num] = True

    # 상자 검색
    for r in [0, 3, 6]:
        for c in [0, 3, 6]:
            chk = [False] * 10
            for y in range(3):
                for x in range(3):
                    num = sudoku[r+y][c+x]
                    if chk[num]:
                        return 0
                    chk[num] = True

    return 1
            

for case in range(1, int(input()) + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{case} {sudoku_check(sudoku)}')
