# 1 Boyer-Moore 알고리즘을 활용한 풀이

def bm_algo(text, pattern):
    i = len(text)
    j = 2

    text_index = 1
    pattern_index = 1
    count = 0
    while text_index < i:
        if text[text_index] == pattern[pattern_index]:
            if pattern_index == 0:
                count += 1
                text_index = text_index + j + 1
                pattern_index = 1
            else:
                text_index -= 1
                pattern_index -= 1
        else:
            while pattern_index >= 0:
                if text[text_index] == pattern[pattern_index]:
                    text_index = text_index + j - (pattern_index + 1)
                    pattern_index = j - 1
                    break
                else:
                    pattern_index -= 1
            if pattern_index == -1:
                text_index = text_index + j
                pattern_index = j - 1
    return count

pattern = ['1', '2']
for case in range(1, 11):
    matrix = []
    length = int(input())
    for numbers in range(length):
        matrix.append(input().split())
    count = 0
    for i in range(length):
        vertical_list = [matrix[j][i] for j in range(length) if matrix[j][i] != '0']
        count += bm_algo(vertical_list, pattern)

    print('#{0} {1}'.format(case, count))


# 2 고지식한 패턴 검색 알고리즘을 활용한 풀이

pattern = ['1', '2']
for case in range(1, 11):
    matrix = []
    length = int(input())
    for numbers in range(length):
        matrix.append(input().split())
    count = 0
    for i in range(length):
        vertical_list = [matrix[j][i] for j in range(length) if matrix[j][i] != '0']
        for j in range(1, len(vertical_list)):
            if pattern == vertical_list[j-1:j+1]:
                count += 1

    print('#{0} {1}'.format(case, count))
    