for case in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    result = [0] * K
    scores = list(map(int, input().split()))
    result[0] = scores[0]
    for score in scores[1:]:
        for i in range(K - 1):
            if i == 0 and score >= result[i]:
                result.insert(i, score)
                result.pop()
                break
            elif result[i] >= score >= result [i + 1]:
                result.insert(i + 1, score)
                result.pop()
                break

    print(f'#{case} {sum(result)}')
