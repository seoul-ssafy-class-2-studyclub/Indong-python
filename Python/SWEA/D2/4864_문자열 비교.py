def bm_algo(text, pattern):
    i = len(text)
    j = len(pattern)

    text_index = j - 1
    pattern_index = j - 1

    while text_index < i:
        if text[text_index] == pattern[pattern_index]:
            if pattern_index == 0:
                return 1
                # return text_index
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
    return 0

case_size = int(input())
if 1 <= case_size <= 50:
    for i in range(case_size):
        str1 = input()
        str2 = input()
        N = len(str1)
        M = len(str2)
        if N <= M:
            result = bm_algo(str2, str1)
            print('#{0} {1}'.format(i + 1, result))
