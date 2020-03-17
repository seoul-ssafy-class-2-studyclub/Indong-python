def my_max(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > result:
            result = numbers[i]
    return result


for case in range(1, 11):
    i = 2
    result = 0
    N = int(input())
    city = list(map(int, input().split()))
    while i <= N - 3:
        if city[i] < city[i+1]:
            i += 1
        elif city[i] < city[i+2]:
            i += 2
        elif city[i-1] > city[i] or city[i-2] > city[i]:
            i += 3
        else:        
            result += (city[i] - my_max([city[i-2], city[i-1], city[i+1], city[i+2]]))
            i += 3

    print(f'#{case} {result}')
