from collections import deque

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 0 - 위 / 1 - 아래 / 2 - 왼쪽 / 3 - 오른쪽 
# 각각의 파이프가 갈 수 있는 방향을 리스트에 저장한다.
# 1번 파이프는 0, 1, 2, 3방향, 2번 파이프는 0, 1방향 ...
pipe = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
# 각각의 방향이 갈 수 있는 파이프의 번호를 기록한다.
# 위로 갈 때는 1, 2, 5, 6번 파이프, 아래로 갈 때는 1, 2, 4, 7번 파이프 ...
can_move = [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]]

for case in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    u = [list(map(int, input().split())) for _ in range(N)]
    # 시작 지점도 구역에 포함되므로 cnt를 1로 설정한다.
    # 시간 단위로 순차적으로 진행되기 때문에 bfs를 실시한다.
    # queue에는 좌표와 파이프 번호를 넣고 지나온 자리를 -1로 만들어 놓는다.
    cnt = 1
    queue = deque()
    queue.append((R, C, u[R][C]))
    u[R][C] = -1
    while L > 1:
        L -= 1
        for _ in range(len(queue)):
            y, x, sh = queue.popleft()
            # 반복문을 통해 파이프에서 갈 수 있는 방향을 불러온다.
            for i in pipe[sh]:
                dy, dx = delta[i]
                yi = y + dy
                xi = x + dx
                # 만약 다음 위치가 범위를 벗어나지 않고, 다음 파이프가 can_move[i] (i는 방향) 안에 있다면
                # cnt를 올리고 queue에 값을 추가한다.
                if 0 <= yi < N and 0 <= xi < M and (u[yi][xi] in can_move[i]):
                    queue.append((yi, xi, u[yi][xi]))
                    cnt += 1
                    u[yi][xi] = -1
    print(f'#{case} {cnt}')
