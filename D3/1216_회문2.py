def manacher_palindrome(string):
    string = '#' + '#'.join(string) + '#'
    N = len(string)
    radius_array = [0] * N
    r = 0
    p = 0
    for i in range(N):
        if i > r:
            radius_array[i] = 0
        else:
            i_apo = (2 * p) - i
            radius_array[i] = min(r - i, radius_array[i_apo])
        while i - radius_array[i] - 1 >= 0 and i + radius_array[i] + 1 < N and string[i - radius_array[i] - 1] == string[i + radius_array[i] + 1]:
            radius_array[i] += 1
        j = i + radius_array[i]
        if j > r:
            r = j
            p = i
    for idx in range(1, N, 2):
        if radius_array[idx] == 1:
            radius_array[idx] = 0
    return radius_array

for case in range(1, 11):
    word_list = []
    number = int(input())
    result = 0
    for i in range(100):
        row = input()
        word_list.append(row)
        max_pal = max(manacher_palindrome(row))
        if result < max_pal:
            result = max_pal
    for j in range(100):
        column = ''
        for k in range(100):
            column += word_list[k][j]
        max_pal = max(manacher_palindrome(column))
        if result < max_pal:
            result = max_pal
    print(f'#{case} {result}')
