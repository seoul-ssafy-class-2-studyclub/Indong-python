def bubble_sort(numbers):
    for i in range(len(numbers)-1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    return numbers

case_size = int(input())
for case in range(1, case_size + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    num_list = bubble_sort(num_list)
    result = num_list[-1] - num_list[0]
    print(f'#{case} {result}')
