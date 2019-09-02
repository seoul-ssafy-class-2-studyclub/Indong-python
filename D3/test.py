for t in range(int(input())):
    N, M, K = map(int, input().split())
    data = list(map(int, input().split()))
    start = 0
    first = data[0]
    for k in range(K):
        start = start + M
        if start <= len(data) - 1:
            data[start:0] = [data[start - 1] + data[start]]
        elif start == len(data):
            data[start:0] = [data[start - 1] + first]
        elif start > len(data):
            start = start - len(data)
            data[start:0] = [data[start - 1] + data[start]]
    print(data[::-1])