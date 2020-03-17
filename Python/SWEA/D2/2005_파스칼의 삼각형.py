dp = [1, 1]

def factorial(n):
    if len(dp) > n:
        return dp[n]
    else:
        result = factorial(n-1) * n
        dp.append(result)
        return result

def print_pascal(x):
    if x == 1:
        print(1)
    else:
        print_pascal(x - 1)
        for i in range(0, x):
            # nCr 구하는 공식 = n! / r!(n-r)!
            number = int(factorial(x - 1) / (factorial(i) * factorial(x - 1 - i)))
            if i == x - 1:
                print(number)
            else:
                print(number, end=' ')


for case in range(1, int(input()) + 1):
    N = int(input())
    print(f'#{case}')
    print_pascal(N)
