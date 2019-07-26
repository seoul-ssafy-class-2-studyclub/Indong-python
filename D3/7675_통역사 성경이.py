# a = 'my name is Hye Soo. my id is Rhs0266. what your id Bro?'
# a = list(a.split())

# case_size = int(input())
# p = ['.', '?', '!']
# for case in range(1, case_size + 1):
#     count_list = []
#     count = 0
#     N = int(input())
#     strings_list = list(input().split())
#     for i in strings_list:
#         if i[0].isupper() and i[-1] not in p:
#             if len(i) == 1 or (i[1:].islower() and i[1:].isalpha()):
#                 count += 1
#         elif i[0].isupper() and i[-1] in p:
#             if len(i) == 2 or (i[1:-1].islower() and i[1:-1].isalpha()):
#                 count += 1
#             count_list += [count]
#             count = 0
#         elif i[-1] in p:
#             count_list += [count]
#             count = 0
#     result = ' '.join(map(str, count_list))
#     print(f'#{case} {result}')

a = 'A.'
print(a.istitle())