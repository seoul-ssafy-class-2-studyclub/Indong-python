a = [2, 2, 2, 1]
b = [1, 2, 3, 4]
def bi_recover(a):
    result = ''
    if abs(a[1] - a[2]) >= 2 or (not (a[1] or a[2]) and (a[0] and a[3])):
        return 'impossible'
    if a[1] > a[2]:
        result += '01' * a[1]
        result = '0' * a[0] + result + '1' * a[3]
    elif a[1] < a[2]:
        result += '10' * a[2]
        result = '1' * a[3] + result + '0' * a[0]
    else:
        if not (a[1] or a[2]):
            if a[0]:
                result = '0' * (a[1] + 1)
            else:
                result = '1' * (a[3] + 1)
        else:
            result = '01' * a[1] + '1' * a[3] + '0' * (a[0] + 1)

    return result

result_list = []
for case in range(1, int(input()) + 1):
    count = list(map(int, input().split()))
    print(f'#{case} {bi_recover(count)}')
