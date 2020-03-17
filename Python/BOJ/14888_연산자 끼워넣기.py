from sys import stdin
def calc(num, p, s, m, d, k=1):
    global min_num, max_num
    if k == N:
        if min_num > num:
            min_num = num
        if max_num < num:
            max_num = num
        return True

    nxt = numbers[k]
    if p > 0:
        calc(num+nxt, p-1, s, m, d, k+1)
    if s > 0:
        calc(num-nxt, p, s-1, m, d, k+1)
    if m > 0:
        calc(num*nxt, p, s, m-1, d, k+1)
    if d > 0:
        calc(int(num/nxt), p, s, m, d-1, k+1)


N = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
plus, sub, mul, div = list(map(int, stdin.readline().split()))
cur = numbers[0]
min_num = 10 ** 9
max_num = (10 ** 9) * -1
calc(cur, plus, sub, mul, div)

print(max_num)
print(min_num)
