import math

def calc(num=0, k=1):
    global max_num, min_num
    if k == N:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
        return
    for i in range(4):
        if ope[i]:
            ope[i] -= 1
            if i == 0:
                calc(num+numbers[k], k+1)
            elif i == 1:
                calc(num-numbers[k], k+1)
            elif i == 2:
                calc(num*numbers[k], k+1)
            else:
                calc(math.trunc(num/numbers[k]), k+1)
            ope[i] += 1


for case in range(1, int(input()) + 1):
    N = int(input())
    ope = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    max_num = -9876987654321
    min_num = 9876987654321
    calc(numbers[0])
    res = max_num - min_num
    print(f'#{case} {res}')
