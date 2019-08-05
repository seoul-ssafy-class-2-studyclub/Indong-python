import random
from pprint import pprint

# # array = [[random.randrange(1, 26) for i in range(5)] for j in range(5)]
# # array = [[3, 6, 18, 5, 21], [9, 10, 20, 18, 11], [23, 15, 14, 6, 3], [25, 1, 8, 5, 5], [6, 3, 10, 1, 6]]
# array = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
# chk_array = [[0] * len(array[0]) for i in range(len(array))]
# pprint(array)
# pprint(chk_array)

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# result_array = [[0] * len(array[0]) for i in range(len(array))]
# for i in range(5):
#     for j in range(5):
#         for k in range(4):
#             xi = i + dx[k]
#             yi = j + dy[k]
#             if 0 <= xi < 5 and 0 <= yi <5:
#                 if chk_array[xi][yi] == '#':
#                     continue
#                 sub_num = array[i][j] - array[xi][yi]
#                 if sub_num < 0:
#                     sub_num *= -1
#                 result_array[i][j] += sub_num
#                 result_array[xi][yi] += sub_num
#         chk_array[i][j] = '#'

# pprint(chk_array)
# pprint(result_array)


array = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], 
[15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]

# array = [[3, 4, 5, 6], [1, 2, 9, 10], [7, 11, 14, 15], [8, 16, 13, 12]]

# 리스트에 array의 값들을 오름차순으로 정렬
num_list = []
for i in range(len(array)):
    for j in range(len(array[0])):
        if i == 0 and j == 0:
            num_list.append(array[i][j])
        elif num_list[-1] < array[i][j]:
            num_list.append(array[i][j])
        else:
            for k in range(len(num_list)):
                if num_list[k] >= array[i][j]:
                    num_list.insert(k, array[i][j])
                    break

print(num_list)
a = 0
b = 0
curve = 1
N = len(array) - 1
while N > 0:
    if curve == 1:
        for i in range(N):
            array[a][b] = num_list.pop(0)
            b += 1
        curve = 2
    elif curve == 2:
        for i in range(N):
            array[a][b] = num_list.pop(0)
            a += 1
        curve = 3
    elif curve == 3:
        for i in range(N):
            array[a][b] = num_list.pop(0)
            b -= 1
        curve = 4
    else:
        for i in range(N - 1):
            array[a][b] = num_list.pop(0)
            a -= 1
        array[a][b] = num_list.pop(0)
        b += 1
        N -= 2
        curve = 1
if len(array) % 2 == 1:
    array[a][b] = num_list.pop(0)
        
pprint(array)
