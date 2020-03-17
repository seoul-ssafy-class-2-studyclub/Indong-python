def calc(equation):
    x = 0
    y = ''
    if equation[0].isdigit():
        equation = '+' + equation
    for num in equation[::-1]:
        if num == '+':
            x += int(y)
            y = ''
        elif num == '-':
            x -= int(y)
            y = ''
        else:
            y = num + y
    return x

print(calc('123+2-124'))
print(calc('-12+12-7979+9191'))
print(calc('+1-1+1-1+1-1'))
