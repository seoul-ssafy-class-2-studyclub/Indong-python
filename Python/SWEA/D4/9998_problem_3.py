# scv는 미네랄과 현재 위치를 왕복해서 이동하므로, 움직이는 거리는 둘 사이의 거리 * 2다.
def calc_dis(idx1, idx2):
    y1, x1 = idx1
    y2, x2 = idx2
    return (abs(y1 - y2) + abs(x1 - x2)) * 2


for case in range(1, int(input()) + 1):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    # 로봇의 위치를 기록할 변수와 미네랄의 위치를 저장할 리스트를 만든다.
    robot_idx = (0, 0)
    mineral_idx = []
    # 길이가 C(로봇이 이동할 수 있는 거리의 총량) + 1인 리스트를 만든다.
    # 이 리스트의 i번째 값은 i만큼 에너지를 썼을 때 얻을 수 있는 미네랄의 최댓값이 기록될 것이다.
    # 순열로 완전탐색을 실시하면 최악의 경우 O(N!)의 시간복잡도가 소요되나,
    # DP를 활용할 시 O(CN)의 시간복잡도 밖에 들지 않는다. (N: 미네랄의 수, C: 최초 에너지)
    dp = [0] * (C + 1)
    for r in range(N):
        for c in range(M):
            if board[r][c] == 1:
                robot_idx = (r, c)
            elif board[r][c]:
                mineral_idx.append((r, c))

    # 미네랄 좌표가 저장되어 있는 리스트에서 좌표를 꺼내며 로봇과 미네랄 사이의 거리, 미네랄의 양을 구한다.
    for idx in mineral_idx:
        dis = calc_dis(robot_idx, idx)
        mineral = board[idx[0]][idx[1]]

        # dp 리스트를 뒤에서부터 확인한다.
        # 뒤에서부터 확인하는 이유는 앞에서부터 dp 리스트를 채워나갈 시 값이 중복으로 처리되는 문제가 발생하기 때문.
        for i in range(C, 0, -1):
            # 만약 dp[i]가 값이 있고 i + dis <= C라면
            # (i만큼 에너지를 쓴 상황에서 미네랄을 가져오기 위해서는 둘의 합이 C보다 작거나 같아야 한다.)
            # i+dis만큼 에너지를 썼을 때의 기존 값이 큰지, i만큼 썼을 때의 값에 현재 미네랄 양을 합친 값이 큰지 비교하여 갱신한다.
            if dp[i] and i + dis <= C:
                dp[i+dis] = max(dp[i+dis], dp[i] + mineral)
        # 순회가 끝나면, dis만큼만 에너지를 썼을 때의 값(맨 처음에 이 미네랄을 가지러 가는 경우) 역시 비교해 준다.
        if dis <= C:
            dp[dis] = max(dp[dis], mineral)

    # dp 리스트 중 최댓값이 구하고자 하는 답이 된다.
    print('#{0} {1}'.format(case, max(dp)))
