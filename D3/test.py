def isIncreasingNum(n):
    temp_list = list(map(int,list(str(n))))
    check = 1
    for i in range(1, len(temp_list)):
        if temp_list[i] < temp_list[i - 1]:
            check = -1
            break
    if  check == -1:
        return False
    else:
        return True

def monotonic(n):
    a = n % 10
    n = int(n / 10)
    while n != 0:
        if n % 10 > a:
            return False
        else:
            a = n % 10
            n = int(n / 10)
    return True
    
test_num = int(input())
for t in range(test_num):
    l = int(input())
    base_list = list(map(int, input().split()))
    result = -1
    for i in range(l - 1):
        for j in range(i+1, l):
            mul = base_list[i] * base_list[j]
            if mul < result:
                continue
            if isIncreasingNum(mul):
                result = mul
   
    print(f'#{t+1} {result}')