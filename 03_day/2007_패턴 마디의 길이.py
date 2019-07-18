case_size = int(input())
try:
    for case in range(case_size):
        word = input()
        if len(word) == 30:
            result = 0
            i = 1
            while i <= 10:
                if word[:i+1] == word[i+1:i+(i+2)]:
                    count_set = set()
                    for j in range(0, len(word) - (len(word) % (i + 1)), i+1):
                        count_set.add(word[j:j+i+1])
                    if len(count_set) > 1:
                        i += 1
                    else:
                        result += len(''.join(list(count_set)[0]))
                        break
                else:
                    i += 1
        else:
            raise ValueError
        print("#{0} {1}".format(case + 1, result))

except ValueError:
    print('올바른 범위의 수를 입력해주세요.')