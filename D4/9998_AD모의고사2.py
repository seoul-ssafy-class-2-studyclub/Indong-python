result_list = []

for case in range(1, int(input()) + 1):
    N = int(input())
    arr = [[[] for i in range(4001)] for j in range(4001)]
    queue = []

    for _ in range(N):
        x, y, dir, energy = map(int, input().split())
        x = (x + 1000) * 2
        y = abs(y - 1000) * 2
        arr[y][x].append(energy)
        queue.append([dir, [y, x]])

    result = 0
    while queue:
        crash = []
        length = len(queue)
        for i in range(length):
            atom = queue.pop(0)
            if not arr[atom[1][0]][atom[1][1]]:
                continue
            energy = arr[atom[1][0]][atom[1][1]].pop()
            is_fin = False
            if atom[0] == 0:
                atom[1][0] -= 1
            elif atom[0] == 1:
                atom[1][0] += 1
            elif atom[0] == 2:
                atom[1][1] -= 1
            elif atom[0] == 3:
                atom[1][1] += 1
            if 0 <= atom[1][0] < 4001 and 0 <= atom[1][1] < 4001:
                if arr[atom[1][0]][atom[1][1]]:
                    is_fin = True
                    if atom[1] not in crash:
                        crash.append(atom[1])
                arr[atom[1][0]][atom[1][1]].append(energy)
                if not is_fin:
                    queue.append(atom)
        for idx in crash:
            result += sum(arr[idx[0]][idx[1]])
            arr[idx[0]][idx[1]].clear()

    result_list.append(result)

for i in range(len(result_list)):
    print('#{0} {1}'.format(i + 1, result_list[i]))   
    
    
