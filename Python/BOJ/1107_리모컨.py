from sys import stdin
# +- 전에 꼭 번호를 N번 누를 필요가 없었다.
# N + 1번까지 확인을 해봐야 했다.


def find_num(n=0, num=0):
    global res
    remote = abs(cha - num) + n
    if res > remote:
        if n >= 1:
            res = remote
    if n == 6 or n == N+1:
        return True

    for i in range(10):
        if B[i]:
            find_num(n+1, num*10+i)


cha = int(stdin.readline())
idx = list(str(cha))
N = len(idx)
M = int(stdin.readline())
broken = list(map(int, stdin.readline().split()))
B = [True] * 10
for i in broken:
    B[i] = False
res = abs(cha - 100)

if res != 0:
    find_num()
print(res)
