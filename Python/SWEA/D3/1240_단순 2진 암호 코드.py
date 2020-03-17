# 모든 코드는 1로 끝나기 때문에 맨 뒷자리를 찾는다.
# 암호코드가 꼭 7의 배수번 째 자리에서 시작한다는 보장이 없기 때문.
def find_end():
    for c in range(M - 1, -1, -1):
        for r in range(N):
            if arr[r][c] == '1':
                return (r, c)
    return 0


code = {'0001101': 0, '0011001': 1, '0010011':2, '0111101': 3, '0100011': 4, '0110001': 5,
'0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    idx = find_end()
    result = 0
    if not idx:
        print(f'#{case} 0')
        continue
    r, c = idx
    password = []
    temp = ''
    for i in range(c, c-56, -1):
        temp = arr[r][i] + temp
        if len(temp) == 7:
            password.insert(0, code[temp])
            temp = ''
    chk = 0
    for i in range(len(password)):
        if not i % 2:
            chk += password[i] * 3
        else:
            chk += password[i]

    if not chk % 10:
        print(f'#{case} {sum(password)}')
    else:
        print(f'#{case} 0')
