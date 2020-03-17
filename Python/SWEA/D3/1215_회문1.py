# def manacher_palindrome(string):
#     string = '#' + '#'.join(string) + '#'
#     N = len(string)
#     radius_array = [0] * N
#     r = 0
#     p = 0
#     for i in range(N):
#         if i > r:
#             radius_array[i] = 0
#         else:
#             i_apo = (2 * p) - i
#             radius_array[i] = min(r - i, radius_array[i_apo])
#         while i - radius_array[i] - 1 >= 0 and i + radius_array[i] + 1 < N and string[i - radius_array[i] - 1] == string[i + radius_array[i] + 1]:
#             radius_array[i] += 1
#         j = i + radius_array[i]
#         if j > r:
#             r = j
#             p = i
#     for idx in range(1, N, 2):
#         if radius_array[idx] == 1:
#             radius_array[idx] = 0
#     return radius_array

# for case in range(1, 11):
#     word_list = []
#     length = int(input())
#     result = 0
#     for i in range(8):
#         row = input()
#         if length % 2:
#             filtering = list(filter(lambda x: x >= length and x % 2, manacher_palindrome(row)))
#         else:
#             filtering = list(filter(lambda x: x >= length and (not x % 2), manacher_palindrome(row)))
#         result += len(filtering)
#         word_list.append(row)
#     for j in range(8):
#         column = ''
#         for k in range(8):
#             column += word_list[k][j]
#         if length % 2:
#             filtering = list(filter(lambda x: x >= length and x % 2, manacher_palindrome(column)))
#         else:
#             filtering = list(filter(lambda x: x >= length and (not x % 2), manacher_palindrome(column)))
#         result += len(filtering)
#     print(f'#{case} {result}')

for case in range(1, 11):
    board = []
    N = int(input())
    cnt = 0
    for r in range(8):
        row = input()
        for i in range(0, 8 - N + 1):
            k = 0
            is_pal = True
            while k < (N // 2):
                if row[i+k] != row[i+N-1-k]:
                    is_pal = False
                    break
                k += 1
            if is_pal:
                cnt += 1
        board.append(row)

    for i in range(0, 8 - N + 1):
        for j in range(8):
            k = 0
            is_pal = True
            while k < (N // 2):
                if board[i+k][j] != board[i+N-1-k][j]:
                    is_pal = False
                    break
                k += 1
            if is_pal:
                cnt += 1
    print(f'#{case} {cnt}')
