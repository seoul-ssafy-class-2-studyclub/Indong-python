T = int(input())
for tc in range(1, T+1):
   N, M = map(int, input().split())
   # 서로 친하다 == 무방향이다
   # 1번이 상원이 그러면 1번이 가진 자식들을 타고 자식과 자식을 타고 가야한다.
   # 1번에 들어갈 자식이 없다면 아무도 없다는 뜻이다.
   adj_list = [[] for _ in range(N+1)]
   for _ in range(1, M+1):
       a, b = map(int, input().split())
       adj_list[a].append(b)
       adj_list[b].append(a)
   result = 0
   visit = [False]*(M+1)
   q = []
   q.append((1, 0))
   visit[1] = True
   while q:
       start, cnt = q.pop(0)
       for child in adj_list[start]:
           # print(child)
           if visit[child] == False and cnt <= 1:
               visit[child] = True
               result += 1
               q.append((child, cnt+1))
   print(f'#{tc}', result)
   