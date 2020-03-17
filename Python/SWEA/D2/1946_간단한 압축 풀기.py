case_size = int(input())
for case in range(1, case_size + 1):
    N = int(input())
    result = []
    word = ''
    for i in range(N):
        alp, number = input().split()
        for cha in range(int(number)):
            word += alp
            if len(word) == 10:
                result += [word]
                word = ''
    result += [word]
    print(f'#{case}')
    for string in result:
        print(string)
