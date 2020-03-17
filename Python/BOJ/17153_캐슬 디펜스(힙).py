from sys import stdin
from heapq import heappop, heappush
from itertools import combinations

# 거리 계산하는 함수
def calc_dis(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)

N, M, D = map(int, input().split())
game = [list(map(int, input().split())) for _ in range(N)]
# 조합을 통해 궁수가 존재할 수 있는 위치를 다 저장해놓는다.
archers = list(combinations(range(M), 3))
# 적들의 좌표도 저장
enemies = [(r, c) for c in range(M) for r in range(N) if game[r][c]]
size = len(enemies)
res = 0

for x, y, z in archers:
    # 1번 궁수(x), 2번 궁수(y), 3번 궁수(z) 각각의 큐를 생성한다.
    q = [[] for _ in range(3)]
    
    # 거리, 열 좌표, 행 좌표, 병졸 번호를 묶어 큐에 삽입한다.
    # 왼쪽에 있을수록 우선순위가 높음.
    for idx, (r, c) in enumerate(enemies):
        heappush(q[0], (calc_dis(N, x, r, c), c, r, idx))
        heappush(q[1], (calc_dis(N, y, r, c), c, r, idx))
        heappush(q[2], (calc_dis(N, z, r, c), c, r, idx))
    
    cnt = 0
    # vis에 적 병사들의 상태를 저장한다. 
    # False(0)은 살아 있음. 1은 화살 맞아 죽음. 2는 밖으로 나감.
    vis = [False] * size
    for i in range(N):
        is_fin = True
        # temp에는 이번 턴의 결과만을 표시한다.
        temp = [False] * size
        # 1번 궁수부터 3번을 보는데,
        for j in range(3):
            if not q[j]:
                continue
            # 큐가 비어 있지 않다면 게임이 끝난 게 아니므로 is_fin을 False로
            is_fin = False
            # shoot는 화살을 쐈는지 안 쐈는지 확인하는 변수
            shoot = False
            nxt_q = []
            for _ in range(len(q[j])):
                dis, c, r, idx = heappop(q[j])
                # 이전 턴에 화살 맞았거나 나갔으면 그냥 넘기고
                if vis[idx]:
                    continue
                # 사정거리 안에 들어왔고 아직 쏜 적 없으면 쏜다.
                if dis <= D and not shoot:
                    temp[idx] = 1
                    shoot = True
                # 나갔으면 2로 처리해주고
                elif r + 1 == N and temp[idx] != 1:
                    temp[idx] = 2
                # 살아 있다면 임시 리스트에 push.
                # 기존 q에 push하면 우선순위 때문에 순서가 꼬일 수 있음.
                else:
                    heappush(nxt_q, (dis - 1, c, r + 1, idx))
            
            q[j], nxt_q = nxt_q, q[j]

        if is_fin:
            break
        # 이번 턴 결과를 vis에 저장해놓는다.
        for j in range(size):
            if temp[j]:
                vis[j] = temp[j]
    
    # 다 끝난 뒤 1 숫자를 센다.
    for chk in vis:
        if chk == 1:
            cnt += 1
    
    if res < cnt:
        res = cnt

print(res)
