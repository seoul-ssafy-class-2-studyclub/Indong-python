def palindrome(word):
    word = word.strip()
    if type(word) != str:
        word = str(word)
    for i in range(int(len(word) / 2)):
        if word[i] != word[-i-1]:
            return 0
    return 1


case_size = int(input())
for case in range(1, case_size + 1):
    char = input()
    result = palindrome(char)
    print(f'#{case} {result}')
