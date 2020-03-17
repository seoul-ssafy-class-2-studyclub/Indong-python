def calc_benefit():
    # 2. K == 1부터 K를 1씩 증가.
    # 설치 위치를 (ym, xm)이라고 했을 때, |ym - yn| + |xm - xn| < K이면 서비스가 제공 가능하다.
    # 반복문을 돌리며 완전탐색.
    global max_cnt
    K = 1
    while True:
        cost = K ** 2 + (K - 1) ** 2
        for r in range(N):
            for c in range(N):
                cnt = 0
                for y, x in houses:
                    dis = abs(y - r) + abs(x - c)
                    if dis < K:
                        cnt += 1
                # 3. 집의 수를 세어 주고 이익 계산
                # 만약 모든 집이 거리 안에 들어와 있으면서 이익이 0보다 작다면, 더 이상 진행할 필요가 없으므로 반복문을 끝낸다. 
                benefit = M * cnt - cost
                if cnt == H and benefit < 0:
                    return False
                if cnt > max_cnt and benefit >= 0:
                    max_cnt = cnt
        K += 1

for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    # 1. 집들의 좌표를 모두 저장함
    houses = []
    H = 0
    for r in range(N):
        for c in range(N):
            if city[r][c]:
                houses.append((r, c))
                H += 1

    max_cnt = 0
    calc_benefit()

    print(f'#{case} {max_cnt}')
