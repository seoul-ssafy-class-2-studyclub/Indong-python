for case in range(1, int(input()) + 1):
    word = input()
    n = len(word)
    cnt_list = [0] * (n + 1)
    H = int(input())

    idx = list(map(int, input().split()))
    for i in idx:
        cnt_list[i] += 1
    
    result = ''
    for i in range(n):
        result += '-' * cnt_list[i] + word[i]
    result += '-' * cnt_list[-1]

    print(f'#{case} {result}')
