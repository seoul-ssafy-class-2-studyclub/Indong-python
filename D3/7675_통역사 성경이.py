a = 'my name is Hye Soo. my id is Rhs0266. what your id Bro?'
a = list(a.split())

p = ['.', '?', '!']
for case in range(1, int(input()) + 1):
    count_list = [0] * int(input())
    idx = 0
    for i in list(input().split()):
        is_number = False
        for j in i:
            if j.isdigit():
                is_number = True
                break
        if not is_number and i.istitle():
            count_list[idx] += 1
        if i[-1] in p:
            idx += 1
    result = ' '.join(map(str, count_list))
    print(f'#{case} {result}')
