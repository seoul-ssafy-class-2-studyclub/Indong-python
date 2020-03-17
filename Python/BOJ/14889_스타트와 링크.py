# stat = [[0, 0, 0, 0, 0],
# [0, 0, 1, 2, 3],
# [0, 4, 0, 5, 6],
# [0, 7, 1, 0, 2],
# [0, 3, 4, 5, 0]]
# N = 4
# vis = [None] + [0] * N


def status(start, link):
    global stat
    global N
    stat_start = 0
    stat_link = 0
    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            stat_start += stat[start[i]][start[j]] + stat[start[j]][start[i]]
            stat_link += stat[link[i]][link[j]] + stat[link[j]][link[i]]
    return abs(stat_start - stat_link)


def team_split(vis, player=1, cnt=1):
    global N
    global min_diff

    vis = vis[:]
    vis[player] = 1
    if cnt == N // 2:
        start = []
        link = []
        for i in range(N + 1):
            if vis[i] == 1:
                start.append(i)
            elif vis[i] == 0:
                link.append(i)
        diff = status(start, link)
        if diff < min_diff or min_diff == -1:
            min_diff = diff

    for i in range(player + 1, N + 1):
        team_split(vis, i, cnt+1)


N = int(input())
vis = [2] + [0] * N
stat = [[0] * (N + 1)]
for i in range(N):
    stat.append([0] + list(map(int, input().split())))
min_diff = -1
team_split(vis)
print(min_diff)