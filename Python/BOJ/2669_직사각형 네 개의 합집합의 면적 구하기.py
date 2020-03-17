from pprint import pprint

graph = [[0] * 100 for i in range(100)]
cnt = 0
for cor in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            if graph[i][j] == 1:
                continue
            graph[i][j] = 1
            cnt += 1
print(cnt)
