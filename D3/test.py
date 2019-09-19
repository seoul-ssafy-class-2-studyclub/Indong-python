def fx(n):
    for i in range(2, n+1):
        f_ls[i] = f_ls[i-2]*2 + f_ls[i-1]

n = int(input())
f_ls = [0] * (n+1)
f_ls[0] = f_ls[1] = 1
fx(n)
print(f_ls[-1] % 10007)