result_list = []
for case in range(int(input())):
    num = input()
    temp = int(num)
    while temp >= 10:
        temp = 0
        for i in num:
            temp += int(i)
        num = str(temp)

    result_list += [num]

for i in range(len(result_list)):
    print(f'#{i + 1} {result_list[i]}')    
    