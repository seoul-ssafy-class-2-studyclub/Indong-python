case_size = int(input())
for case in range(1, case_size + 1):
    number_set = set()
    sheep = int(input())
    i = 1
    while True:
        number_set.update(str(sheep * i))
        if len(number_set) == 10:
            print(f'#{case} {sheep * i}')
            break
        else:
            i += 1
