'''
https://sarah950716.tistory.com/12
http://printf.egloos.com/v/755618
'''

case_size = int(input())
for case in range(1, case_size + 1):
    N, M = map(int, input().split())
    adjacency_list = [[] for i in range(N + 1)]
    count = 0
    for i in range(M):
        x, y = map(int, input().split())
        adjacency_list[x].append(y)
        adjacency_list[y].append(x)
    for i in range(1, N + 1):
        for j in adjacency_list[i]:
            if j < i :
                continue
            else:
                for k in adjacency_list[j]:
                    if k < j:
                        continue
                    elif i in adjacency_list[k]:
                        count += 1
    print(f'#{case} {count}')
