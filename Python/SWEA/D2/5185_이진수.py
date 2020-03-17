# 0 ~ 9: 48 ~ 57
# A ~ F : 65 ~ 70

zero = ord('0')  # 48
nine = ord('9')  # 57
A = ord('A')  # 65
for case in range(1, int(input()) + 1):
    N, hex_num = input().split(' ')
    result = ''
    for i in list(hex_num):
        val = ord(i)
        if val > nine:
            val = val - A + 10
        else:
            val = val - zero

        temp = ''
        for k in range(4):
            if val & 1:
                temp = '1' + temp
            else:
                temp = '0' + temp
            val = val >> 1
        result += temp

    print(f'#{case} {result}')
