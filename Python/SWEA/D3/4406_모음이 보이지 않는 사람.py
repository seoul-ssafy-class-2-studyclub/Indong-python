vowels = ['a', 'e', 'i', 'o', 'u']
for case in range(1, int(input()) + 1):
    word = list(input())
    result = ''
    for char in word:
        if char not in vowels:
            result += char
    print(f'#{case} {result}')
    