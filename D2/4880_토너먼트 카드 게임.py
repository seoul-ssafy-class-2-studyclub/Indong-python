adj = [None, 3, 1, 2]

def tour(cards):
    if len(cards) == 1:
        return cards[0]
    middle = (len(cards) - 1) // 2
    a = tour(cards[:middle+1])
    b = tour(cards[middle+1:])
    if a[1] == b[1]:
        return a
    elif adj[a[1]] == b[1]:
        return a
    else:
        return b


for case in range(1, int(input()) + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    cards = [i for i in enumerate(cards)]
    print(f'#{case} {tour(cards)[0] + 1}')
