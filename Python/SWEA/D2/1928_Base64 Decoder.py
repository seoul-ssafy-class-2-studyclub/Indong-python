# # 대문자: 65 ~ 90
# # 소문자: 97 ~ 112
# # 숫자: 48 ~ 57

def ToBinary(x):
    result = ''
    while True:
        if x == 1:
            result += '1'
            break
        result += str(x % 2)
        x = x // 2
    if len(result) != 6:
        result += '0' * (6 - len(result))
    return result[::-1]

case_size = int(input())
for case in range(1, case_size + 1):
    encoded_word = input()
    before_decoding = ''
    decoded_word = ''
    for cha in encoded_word:
        if cha.isupper():
            before_decoding += ToBinary(ord(cha) - 65)
        elif cha.islower():
            before_decoding += ToBinary(ord(cha) - 71)
        elif cha.isdigit():
            before_decoding += ToBinary(ord(cha) + 4)
        elif cha == '+':
            before_decoding += ToBinary(62)
        elif cha == '/':
            before_decoding += ToBinary(63)

    for i in range(0, len(before_decoding), 8):
        decoded_word += chr(int(before_decoding[i:i+8], 2))
    print(f'#{case} {decoded_word}')
