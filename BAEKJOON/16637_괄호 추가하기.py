import sys
from math import ceil

def calc(a, b, ope):
    if ope == '+':
        return a + b
    elif ope == '-':
        return a - b
    else:
        return a * b


def find_max(left=0, total=0):
    global res
    if left >= end:
        if res < total:
            res = total
        return
    
    ope = expr[left*2-1]
    find_max(left+1, calc(total, int(expr[left*2]), ope))
    if left < end - 1:
        find_max(left+2, calc(total, subtotal[left], ope))


input = sys.stdin.readline
N = int(input())
expr = input()
end = ceil(N / 2)
subtotal = [0] * (N // 2)
for i in range(0, N - 2, 2):
    a = int(expr[i])
    ope = expr[i+1]
    b = int(expr[i+2])
    subtotal[i//2] = calc(a, b, ope)

res = -2 ** 31
find_max(1, int(expr[0]))
if N // 2 > 1:
    find_max(2, subtotal[0])
print(res)
