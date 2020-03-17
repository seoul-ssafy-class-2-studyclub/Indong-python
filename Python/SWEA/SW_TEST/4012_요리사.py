def comb(k=1, s=1):
    global ans
    if k == R:
        food1 = food2 = 0
        x = list(set([x for x in range(N)]) - set(t))
        for i in range(R - 1):
            for j in range(i + 1, R):
                food1 += (ingredients[t[i]][t[j]] + ingredients[t[j]][t[i]])
                food2 += (ingredients[x[i]][x[j]] + ingredients[x[j]][x[i]])
        ans = min(ans, abs(food1 - food2))
        return
    for i in range(s, N + (k - R) + 1):
        t[k] = i
        comb(k+1, i+1)


for case in range(1, int(input()) + 1):
    N = int(input())
    R = N // 2
    t = [0] * R
    ingredients = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321
    comb()
    print(f'#{case} {ans}')
