# set, sort, int 안 쓰고 풀기

def stoi(x):
    zero = ord('0')
    A = ord('A')
    cur = ord(x)
    if cur >= A:
        return cur - A + 10
    return cur - zero


def hextodem(x):
    res = 0
    for i in range(len(x)):
        res += (16 ** i) * stoi(x[-1-i])
    return res


def qsort(arr):
    L = len(arr)
    if L <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    equal = [pivot]
    for i in range(L):
        cur = arr[i]
        if cur > pivot:
            left.append(cur)
        elif cur < pivot:
            right.append(cur)
    return qsort(left) + equal + qsort(right)


for case in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    interval = N // 4
    password = list(input())
    cand = []

    for _ in range(interval):
        for i in range(0, N, interval):
            cand.append(hextodem(''.join(password[i:i+interval])))
        password.append(password.pop(0))

    print(f'#{case} {qsort(cand)[K-1]}')
