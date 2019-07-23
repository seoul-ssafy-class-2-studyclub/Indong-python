def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
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

case_size = int(input())
try:
    for case in range(case_size):
        N = int(input())
        if 1 <= N <= 10:
            print(f'#{case + 1}')
            print_pascal(N)
        else:
            raise ValueError
except ValueError:
    print('올바른 범위의 수를 입력해주세요.')
