dt = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# y, x - 좌표
# k - 깎을 수 있는 최대 높이
# cnt - 경로의 길이
def dfs(y, x, k, cnt=1):
    global max_cnt
    now = mountain[y][x]
    for b, a in dt:
        yi = y + b
        xi = x + a
        if 0 <= yi < N and 0 <= xi < N:
            nxt = mountain[yi][xi]
            # 네 방향을 탐색하면서 현재(now)보다 다음 위치(nxt)가 낮다면,
            # 현재 위치를 100으로 만들어 주고 재귀 호출을 실시한다.
            # 현위치의 값을 안 바꾸면 이후 호출에서 앞서 지나온 길을 깎고 돌아갈 수 있기 때문.
            if nxt < now:
                mountain[y][x] = 100
                dfs(yi, xi, k, cnt+1)
                mountain[y][x] = now
            # 만약 k가 0이 아니고, nxt에서 k를 뺀 값(깎았을 때의 높이)이 현재보다 낮다면,
            # 다음 높이를 현재 높이에서 1만큼 빼준 값으로 변환하고(더 낮게 만들 필요가 없다.)
            # 현재 위치를 100으로 만들어 준 뒤 재귀 호출을 실행한다. 
            # 이때 k를 0으로 바꿔서 공사 기회를 차감한다.
            elif k and nxt - k < now:
                mountain[yi][xi] = now - 1
                mountain[y][x] = 100
                dfs(yi, xi, 0, cnt+1)
                mountain[yi][xi] = nxt
                mountain[y][x] = now
            # 더 이상 길을 만들 수 없다면 현재 저장되어 있는 최댓값과 지금 경로 길이를 비교하여 값을 갱신한다.
            else:
                if max_cnt < cnt:
                    max_cnt = cnt


for case in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    # altitude = 정상 고도를 저장할 변수
    # peaks = 봉우리의 좌표를 담을 리스트
    altitude = 0
    peaks = []
    for j in range(N):
        for i in range(N):
            temp = board[j][i]
            # 만약 board[j][i]의 값이 현재 저장되어 있는 고도보다 크다면 이를 갱신하고
            # peaks를 [(j, i)]로 바꾸어 준다.
            if temp > altitude:
                altitude = temp
                peaks = [(j, i)]
            # 현재 최고 높이와 같다면 peaks에 좌표를 추가해 준다.
            elif temp == altitude:
                peaks.append((j, i))

    max_cnt = 0
    for i in range(len(peaks)):
        # peaks에 저장되어 있는 좌표 하나하나에 대해 완전탐색을 실시.
        # 탐색 시 산이 깎여나갈 것이므로 산을 복사해둔다.
        mountain = [row[:] for row in board]
        y, x = peaks[i]
        dfs(y, x, K)

    print(f'#{case} {max_cnt}')
