def move(wait, dis, cnt):
    minute = 0
    wait_cnt = 3
    while cnt > 0:
        minute += 1
        if minute > min_time:
            return minute
        out = wait.pop(0)
        wait_cnt += out
        cnt -= out
        wait.append(0)
        if cnt == 0:
            break
 
        if wait_cnt != 0:
            down = dis[0]
            if down <= wait_cnt:
                wait[-1] += down
                wait_cnt -= down
                dis[0] = 0
            else:
                wait[-1] += wait_cnt
                dis[0] -= wait_cnt
                wait_cnt = 0
 
        if len(dis) > 1:
            for i in range(1, len(dis)):
                if i == 1:
                    dis[i-1] += dis[i]
                else:
                    dis[i-1] = dis[i]
            dis.pop()
    return minute
 
 
for case in range(1, int(input()) + 1):
    N = int(input())
    room = [(list(map(int, input().split()))) for _ in range(N)]
    people = []
    stair = []
    wait1 = []
    wait2 = []
    for i in range(N):
        for j in range(N):
            if room[i][j] == 1:
                people.append((i, j))
            elif room[i][j] > 1:
                stair.append((i, j))
                if wait1:
                    wait2 = [0] * room[i][j]
                else:
                    wait1 = [0] * room[i][j]
    dis1 = []
    dis2 = []
    s1, s2 = stair[0], stair[1]
     
    for person in people:
        dis1.append(abs(s1[0] - person[0]) + abs(s1[1] - person[1]))
    for person in people:
        dis2.append(abs(s2[0] - person[0]) + abs(s2[1] - person[1]))
     
    min_time = 9999
    n = len(people)
    l_t = (N - 1) * 2 + 1
    for i in range(1 << n):
        time1 = [0 for _ in range(l_t)]
        time2 = [0 for _ in range(l_t)]
        cnt1 = 0
        cnt2 = 0
        for j in range(n):
            if i & (1 << j):
                time1[dis1[j]] += 1
                cnt1 += 1
            else:
                time2[dis2[j]] += 1
                cnt2 += 1
        m1 = move(wait1[:], time1, cnt1)
        m2 = move(wait2[:], time2, cnt2)
        temp = max(m1, m2)
        if min_time > temp:
            min_time = temp
 
    print(f'#{case} {min_time}')
    