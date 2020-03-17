def manacher_palindrome(string):
    string = '#' + '#'.join(string) + '#'
    N = len(string)
    A = [0] * N
    r = 0
    p = 0
    for i in range(N):
        if i > r:
            A[i] = 0
        else:
            i_apo = (2 * p) - i
            A[i] = min(A[i_apo], r - i)
        while i - A[i] - 1 >= 0 and i + A[i] + 1 < N and string[i - A[i] - 1] == string[i + A[i] + 1]:
            A[i] += 1
        j = i + A[i]
        if j > r:
            r = j
            p = i
    for idx in range(1, N, 2):
        if string[idx] == 1:
            string[idx] = 0
    return A

case_size = int(input())
for case in range(1, case_size + 1):
    m = input()
    result = max(manacher_palindrome(m))
    print(f'#{case} {result}')
    