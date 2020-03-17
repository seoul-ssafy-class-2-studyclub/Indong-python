def bm_algo(text, pattern):
    i = len(text)
    j = len(pattern)

    text_index = j - 1
    pattern_index = j - 1
    count = 0
    while text_index < i:
        if text[text_index] == pattern[pattern_index]:
            if pattern_index == 0:
                count += 1
                text_index = text_index + j + 1
                pattern_index = j - 1
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


for case in range(1, 11):
    N = int(input())
    pattern_text = input()
    string = input()
    print(f'#{case} {bm_algo(string, pattern_text)}')
    