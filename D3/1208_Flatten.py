def dump(box_list, num):
    box_list = sorted(box_list, reverse=True)
    i = 0
    j = -1
    for k in range(num):
        box_list[i] -= 1
        box_list[j] += 1
        if box_list[i] < box_list[i+1]:
            i += 1
        else:
            i = 0
        if box_list[j-1] < box_list[j]:
            j -= 1
        else:
            j = -1

    return box_list[i] - box_list[j]


for case in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    print(f'#{case} {dump(boxes, N)}')
