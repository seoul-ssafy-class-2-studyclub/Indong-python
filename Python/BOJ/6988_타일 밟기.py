from sys import stdin

N = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
limit = max(numbers)
a = [False] * (limit + 1)
for num in numbers:
    a[num] = True

max_sum = 0
for i in range(N):
    start = numbers[i]
    for j in range(i + 1, N):
        path = start
        diff = numbers[j] - start
        nxt = start + diff
        cnt = 1
        while nxt <= limit:
            chk = a[nxt]
            if chk:
                path += nxt
                cnt += 1
            else:
                break
            nxt += diff
        if cnt > 2 and path > max_sum:
            max_sum = path

print(max_sum)
