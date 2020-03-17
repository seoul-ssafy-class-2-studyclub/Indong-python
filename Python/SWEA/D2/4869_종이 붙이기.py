DP = [0, 1, 3]

def paper(x):
    global DP
    if len(DP) > x:
        return DP[x]
    result = paper(x-2)*2 + paper(x-1)
    DP.append(result)
    return result

for case in range(1, int(input()) + 1):
    N = int(input()) // 10
    print(f'#{case} {paper(N)}')
    