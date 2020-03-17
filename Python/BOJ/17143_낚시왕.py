import sys
from pprint import pprint

# 움직임이 끝났을 때 위치랑 방향 구하는 함수
def calc(idx_s, w, speed, di):
    while True:
        idx_s += speed
        if 0 <= idx_s <= w:
            return idx_s, di
        if idx_s >= w:
            speed = w - idx_s
            idx_s = w
            if di == 2:
                di = 1
            elif di == 3:
                di = 4
        if idx_s <= 0:
            speed = abs(idx_s)
            idx_s = 0
            if di == 1:
                di = 2
            elif di == 4:
                di = 3
        

R, C, M = map(int, sys.stdin.readline().split())
# sharks: 상어들의 정보, board: 현재 상어들의 위치, chk: 이동한 상어들은 여기로 들어감
sharks = []
board = [[0 for i in range(C)] for _ in range(R)]
chk = [[0 for i in range(C)] for _ in range(R)]
for i in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    r, c = r - 1, c - 1
    sharks.append([r, c, s, d, z])
	# 복사(sharks[-1][:])가 아니라 참조!
    board[r][c] = sharks[-1]

fish = 0
for i in range(C):
	# 낚시꾼이 상어 잡고
    for j in range(R):
        if board[j][i]:
            fish += board[j][i][4]
		    # 죽은 상어는 크기를 -1로 바꿔줌. 위에서 복사가 아니라 참조로 해줬기 때문에 
		    # board를 바꾸면 sharks 안의 값까지 같이 바꿔줄 수가 있다.
            board[j][i][4] = -1
            board[j][i] = 0
            break

    for j in range(len(sharks)):
        r, c, s, d, z = sharks[j]
		# 죽은 상어면 지나가고
        if z == -1:
            continue
        board[r][c] = 0
        
		# 방향에 따라서 이동하게 만든다.
        if d == 1:
            r, d = calc(r, R - 1, -s, d)
        elif d == 2:
            r, d = calc(r, R - 1, s, d)
        elif d == 3:
            c, d = calc(c, C - 1, s, d)
        elif d == 4:
            c, d = calc(c, C - 1, -s, d)
        sharks[j][0] = r
        sharks[j][1] = c
        sharks[j][3] = d
        
		# 이동하려는 곳에 아직 아무 상어도 없으면 그냥 집어넣고(이때도 복사가 아니라 참조)
        if not chk[r][c]:
            chk[r][c] = sharks[j]
		# 상어가 있다면 크기를 비교해서 작은 상어의 크기를 -1로 바꿔준다.
        else:
            if chk[r][c][4] < sharks[j][4]:
		        # 이때 chk[r][c][4]가 -1로 바뀌면서 sharks에 있는 녀석도 같이 바뀐다.
                chk[r][c][4] = -1
                chk[r][c] = sharks[j]
            else:
                sharks[j][4] = -1
    # board가 텅 비었을 테니 둘을 바꿔준다.
    board, chk = chk, board

print(fish)
