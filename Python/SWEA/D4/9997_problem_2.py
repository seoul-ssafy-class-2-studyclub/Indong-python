def calc_dis(idx1, idx2):
    # idx1과 idx2는 각각 로봇과 쿠키의 좌표.
    # 로봇과 쿠키 사이의 거리는 |y1 - y2| + |x1 - x2|와 같다.
    y1, x1 = idx1
    y2, x2 = idx2
    return abs(y1 - y2) + abs(x1 - x2)


# dis는 누적 거리합, k는 몇 번째 로봇까지 봤는지
def find_cookie(dis=0, k=0):
    global res
    # k == 6이라면 모든 로봇을 확인했으므로 res와 dis를 비교 및 교체한다.
    if k == 6:
        if res > dis:
            res = dis
        return
    # 기존에 저장되어 있는 res보다 dis가 더 크다면, 더 이상 확인할 필요가 없으므로 분기를 끝낸다(백트래킹).
    if res < dis:
        return
    for i in range(6):
        # 아직 찾은 적이 없는 쿠키라면 방문 시작.
        if not vis[i]:
            vis[i] = True
            # 기존 누적 거리에 k번 로봇과 i번 쿠키 사이의 거리를 합치고 재귀호출을 실시한다.
            temp = dis + calc_dis(robot_idx[k], cookie_idx[i])
            find_cookie(temp, k+1)
            vis[i] = False


for T in range(int(input())):
    case = int(input())
    board = [list(map(int, input().split())) for _ in range(10)]
    robot_idx = []
    cookie_idx = []
    vis = [False] * 6
    for r in range(10):
        for c in range(10):
            if board[r][c] == 9:
                robot_idx.append((r, c))
            elif board[r][c]:
                cookie_idx.append((r, c))
    res = 987654321
    find_cookie()
    print('#{0} {1}'.format(case, res))
