case_size = int(input())
p = ['.', '?', '!']
for case in range(1, case_size + 1):
    count_list = []
    count = 0
    N = int(input())
    strings_list = list(input().split())
    for i in strings_list:
        if len(i) == 1 and i.isupper():
            count += 1
        elif not i[-1].isdigit() and i[:-1].isalpha() and i.istitle():
            count += 1
        if i[-1] in p:
            count_list += [count]
            count = 0        
    result = ' '.join(map(str, count_list))
    print(f'#{case} {result}')
