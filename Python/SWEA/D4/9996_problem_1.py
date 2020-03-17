for case in range(1, int(input()) + 1):
    N = int(input())
    roads = [list(map(int, input().split())) for _ in range(N)]

    # '_번째 열/행을 모두 idx로 만들기 위해 필요한 비용'을 저장하는 리스트를 만든다.
    row = [[0] * 6 for _ in range(N)]
    col = [[0] * 6 for _ in range(N)]

    # 1부터 6까지 확인
    for i in range(1, 6):
        for r in range(N):
            for c in range(N):
                # 높이를 i로 만드는 비용은 |i - 현재 높이|
                diff = abs(i - roads[r][c])
                # r번째 행과 c번째 열을 i로 만드는 비용 합계에 각각 더한다.
                row[r][i] += diff
                col[c][i] += diff

    res = 987654321
    height = 0
    for r in range(N):
        for c in range(N):
            for i in range(1, 6):
                # temp는 r번째 행과 c번째 열을 i로 만드는 총비용이다.
                # abs(i - roads[r][c])를 빼준 것은 이 위치가 중복해서 더해지기 때문.
                # A & B = A + B - A|B의 원리와 같다.
                temp = row[r][i] + col[c][i] - abs(i - roads[r][c])
                # temp가 res보다 작다면 res를 temp로, height를 i로 교체
                if temp < res:
                    res = temp
                    height = i
                # temp와 res가 같고 i가 height보다 작다면 height만 i로 바꾼다.
                elif temp == res and i < height:
                    height = i

    print('#{0} {1} {2}'.format(case, res, height))
