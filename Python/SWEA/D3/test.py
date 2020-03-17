# 1.
def hitAndSpread(ar, vi, id):
    q = []
    # 앞에서 부터
    for y in range(H):
        if ar[y][id] != 0:
            q.append((y, id))
            vi[y][id] = True
    # vi에 퍼진애만 체크한다.
    # 퍼질애는 다 퍼졌는가?
    # ar은 그냥 참고용
    while q:
        y, x = q.pop(0)
        ########### 처리 확인해야 한다.
        if ar[y][x] == 1:
            # 1이라면 아래 할 필요없이 다른걸 꺼낸다.
            vi[y][x] = True
            continue
        else:
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                # 하나 돌때마다 증가되어야하니까
                # 원본을 복사해두고 시작
                ory = y
                orx = x
                for i in range(0, ar[y][x] - 1):
                    iy = ory + dy
                    ix = orx + dx
                    if 0 <= iy < H and 0 <= ix < W and vi[iy][ix] == False and ar[iy][ix] != 0:
                        vi[iy][ix] = True
                        q.append((iy, ix))
                    ory = iy
                    orx = ix
    return ar, vi
​
​
# 2.
def popping(ar, vi):
    for y in range(H):
        for x in range(W):
            if vi[y][x] == True:
                ar[y][x] = 0
    return ar
​
​
# 3.
def gravity(ar):
​
    # 위로 올라가면서 0으로 바꿔가며 쌓고,
    # 위로 올라가면서 다시 놓는다
    stack = []
    for x in range(W, 0, -1):
        for y in range(H, 0, -1):
            print(y, x)
            if ar[y][x] != 0:
                stack.append(ar[y][x])
                ar[y][x] = 0
​
        for x in range(W, 0, -1):
            for y in range(H, 0, -1):
                data = stack.pop(0)
                ar[y][x] = data
    return ar
​
​
​
​
# 4.
def check(ar):
    cnt = 0
    for y in range(H):
        for x in range(W):
            if ar[y][x] != 0:
                cnt += 1
    return cnt
​
​
​
​
def solve(t):
    global mymin, origin
    arr = [i[:] for i in origin]
    # print(arr)
    # print(t)
    # 작업 시작하는 함수
    while t:
        idx = t.pop()
        vis = [[False]*W for _ in range(H)]
        arr, vis = hitAndSpread(arr, vis, idx)
        arr = popping(arr, vis)
        arr = gravity(arr)
    mymin = min(mymin, check(arr))
    return
​
​
def permut(k):
    if k == N:
        print(t)
        solve(t)
        return
    else:
        for i in range(0, W):
            t[k] = wIndexes[i]
            permut(k+1)
​
​
T = int(input())
for tc in range(1, T-3):
    N, W, H = map(int, input().split())
    print(N, W, H)
    origin = [list(map(int, input().split())) for _ in range(H)]
    mymin = 1e9
    wIndexes = [i for i in range(W)]
    t = [0]*N
    permut(0)
    print(mymin)