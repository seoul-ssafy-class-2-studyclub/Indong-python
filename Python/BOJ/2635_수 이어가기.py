def sub_fibo(a, b):
    cnt = 2
    a = a
    b = b
    result = f'{a} {b}'
    while a >= b:
        cnt += 1
        a, b = b, a - b
        result += ' ' + str(b)
    return cnt, result

N = int(input())
max_cnt = 0
result = ''
for i in range(N // 2, N + 1):
    s_f = sub_fibo(N, i)
    if s_f[0] > max_cnt:
        max_cnt = s_f[0]
        result = s_f[1]

print(max_cnt)
print(result)
