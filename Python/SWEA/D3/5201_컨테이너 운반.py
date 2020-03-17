for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    container = sorted(list(map(int, input().split())))
    truck = sorted(list(map(int, input().split())))
    res = 0
    while truck:
        is_fin = True
        temp = truck.pop()
        while container:
            cargo = container.pop()
            if temp >= cargo:
                res += cargo
                is_fin = False
                break
        if is_fin:
            break

    print(f'#{case} {res}')
