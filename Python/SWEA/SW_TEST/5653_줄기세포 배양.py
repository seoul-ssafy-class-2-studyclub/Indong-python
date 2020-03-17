from collections import deque

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for case in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    vessel = [list(map(int, input().split())) for _ in range(N)]
    # 그리드 셀 방문 여부를 확인하기 위한 2차원 배열을 만든다.
    # 줄기세포의 크기가 1시간마다 커질 것을 가정하여(최악의 상황) 배열의 규모를 정한다.
    vis = [[False] * (M + (K * 2)) for _ in range(N + (K * 2))]
    # cells - 세포들의 정보가 담길 리스트
    # alive - 살아 있는 세포들의 수
    cells = []
    alive = 0
    for r in range(N):
        for c in range(M):
            vit = vessel[r][c]
            if vit:
                # r, c, vit, act, life - y좌표, x좌표, 생명력, 활성화 여부, 수명
                # 방문 여부를 표시하고, alive를 1씩 올린다.
                cells.append((r, c, vit, vit, vit))
                vis[r][c] = True
                alive += 1
    
    # cells를 x[2](생명력) 기준으로 내림차순 정렬한다.
    # 무조건 생명력 수치가 큰 세포부터 확산을 시작하기 때문에
    # 같은 자리에 도착한 세포들을 추가적으로 중복 처리할 필요가 없다.
    cells = deque(sorted(cells, key=lambda x: x[2], reverse=True))
    for _ in range(K):
        # pop - append 과정에서 죽은 세포는 다시 넣지 않을 것이므로,
        # 살아 있는 세포들의 수로 범위를 설정한다.
        # len(cells)을 할 필요가 없음.
        for i in range(alive):
            y, x, vit, act, life = cells.popleft()
            # act를 1씩 줄여나가다 0이 되는 순간 활성 상태로 변한다.
            # 0이 됨과 동시에 번식을 하는 건 아니므로 밑의 조건문을 elif로 처리한다.
            if act > 0 :
                act -= 1
                cells.append((y, x, vit, act, life))
            # 0(활성 상태)라면 번식을 시작한다.
            elif act == 0:
                # 생명력을 1 줄이고 네 방향을 탐색한다.
                life -= 1
                for b, a in delta:
                    yi = y + b
                    xi = x + a
                    # 진행 방향에 세포가 존재하지 않는다면 방문 여부를 표시하고 새로운 세포의 정보를 cells에 추가한다.
                    # 세포가 하나 늘어났으므로 alive를 1 올려준다.
                    if not vis[yi][xi]:
                        vis[yi][xi] = True
                        cells.append((yi, xi, vit, vit, vit))
                        alive += 1
                # 번식이 끝나고 생명력이 0이 됐다면 alive를 1 줄인다.
                if life == 0:
                    alive -= 1
                # 생명력이 0이 아닌 세포만 다시 cells에 append한다.
                else:
                    cells.append((y, x, vit, act, life))

    print(f'#{case} {alive}')
