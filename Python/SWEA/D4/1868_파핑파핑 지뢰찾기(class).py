import sys
sys.stdin = open('input.txt', 'r')

class Board:
    def __init__(self, board, N):
        self.board = board
        self.N = N
        self.count = 0


class Openmine:
    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.game = game
    
    def mkcdn(self):
        cdn =  [(self.x - 1, self.y), (self.x - 1, self.y + 1), (self.x, self.y + 1), (self.x + 1, self.y + 1), (self.x + 1, self.y), 
        (self.x + 1, self.y - 1), (self.x, self.y - 1), (self.x - 1, self.y - 1)]
        return cdn

    def chkmine(self):
        mine_chk = False
        zero_chk = False
        cdn = self.mkcdn()
        for i in cdn:
            if (-1 in i) or (self.game.N in i):
                continue
            elif mine_chk and zero_chk:
                break
            elif self.game.board[i[0]][i[1]] == '*':
                mine_chk = True
            elif self.game.board[i[0]][i[1]] == 0:
                zero_chk = True

        if mine_chk and not zero_chk:
            self.game.board[self.x][self.y] = 2
            self.game.count += 1
        elif mine_chk and zero_chk:
            self.game.board[self.x][self.y] = 1
        elif not mine_chk:
            self.game.board[self.x][self.y] = 0
            if not zero_chk:
                self.game.count += 1
            for j in cdn:
                if (-1 in j) or (self.game.N in j):
                    continue
                elif self.game.board[j[0]][j[1]] == 2:
                    self.game.board[j[0]][j[1]] = 1
                    self.game.count -= 1
                elif self.game.board[j[0]][j[1]] == '.':
                    Openmine(j[0], j[1], self.game).chkmine()


case_size = int(input())
for case in range(1, case_size + 1):
    N = int(input())
    matrix = []
    for row in range(N):
        matrix.append([char for char in input()])
    game_board = Board(matrix, N)
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '.':
                Openmine(i, j, game_board).chkmine()
    print(f'#{case} {game_board.count}')
