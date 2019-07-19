def conut_subtotal(x, y):
    result = 0
    for number in range(len(x) - (y - 1)):
        subtotal_number = sum(x[number:number+y])
        if subtotal_number == y:
            if number == 0:
                if x[y] == 1:
                    continue
                else:
                    result += 1
            elif number == len(x) - y:
                if x[number - 1] == 1:
                    continue
                else:
                    result += 1
            else:
                if x[number - 1] or x[number + y] == 1:
                    continue
                else:
                    result += 1
    return result


case_size = int(input())
list_result = []
try:
    for case in range(case_size):
        puzzle_length, word_length = map(int, input().split()) 
        result = 0
        square_list = []
        if (5 <= puzzle_length <= 15) and (2 <= word_length <= puzzle_length):
            for i in range(puzzle_length):
                horizonal_list = list(map(int, input().split()))
                square_list += [horizonal_list]
                result += conut_subtotal(horizonal_list, word_length)

            for j in range(puzzle_length):
                vertical_list = [l[j] for l in square_list]
                result += conut_subtotal(vertical_list, word_length)
            list_result += [result]
        else:
            raise ValueError

    for key, value in enumerate(list_result):
        print(f"#{key + 1} {value}")

except ValueError:
    print("범위 내의 숫자를 입력해주세요.")
