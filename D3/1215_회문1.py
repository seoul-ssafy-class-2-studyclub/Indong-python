# manacher algorithm을 이용한 풀이
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
    length = int(input())
    result = 0
    for i in range(8):
        row = input()
        if length % 2:
            filtering = list(filter(lambda x: x >= length and x % 2, manacher_palindrome(row)))
        else:
            filtering = list(filter(lambda x: x >= length and (not x % 2), manacher_palindrome(row)))
        result += len(filtering)
        word_list.append(row)
    for j in range(8):
        column = ''
        for k in range(8):
            column += word_list[k][j]
        if length % 2:
            filtering = list(filter(lambda x: x >= length and x % 2, manacher_palindrome(column)))
        else:
            filtering = list(filter(lambda x: x >= length and (not x % 2), manacher_palindrome(column)))
        result += len(filtering)
    print(f'#{case} {result}')

