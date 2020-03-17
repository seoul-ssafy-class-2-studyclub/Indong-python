def dump(box_list, num):
    # 박스의 높이가 담긴 리스트를 내림차순으로 정렬
    # 정렬된 리스트가 48 48 47 47 ... 이라고 가정
    box_list = sorted(box_list, reverse=True)
    i = 0
    j = -1
    for k in range(num):
        # 0번째 인덱스(가장 큰 값)을 하나 빼주고, -1번째 인덱스(가장 작은 값)을 하나 더해준다.
        # <47> 48 47 47 ...
        box_list[i] -= 1
        box_list[j] += 1
        # 만약 다음 인덱스의 값이 현재 인덱스보다 크다면 인덱스를 옆으로 옮긴다.
        # 47 <48> 47 47 ...
        # 한 번 더 반복한다면 47 <47> 47 47 ...이 되어 있을 것
        if box_list[i] < box_list[i+1]:
            i += 1
        # 다음 인덱스의 값이 현재 인덱스보다 작거나 같다면 처음으로 인덱스를 옮긴다.
        # <47> 47 47 47 ...
        else:
            i = 0
        # 큰 값을 빼는 동시에 작은 값에 더해주는 과정 
        if box_list[j-1] < box_list[j]:
            j -= 1
        else:
            j = -1
    # 반복이 끝났을 때 최댓값의 인덱스가 i, 최솟값의 인덱스가 j가 된다.
    return box_list[i] - box_list[j]


for case in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    print(f'#{case} {dump(boxes, N)}')
