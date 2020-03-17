def alien_qsort(arr):
    alien_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5,
"SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    left = []
    equal = []
    right = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for x in arr:
            if alien_dict[x] < alien_dict[pivot]:
                left += [x]
            elif alien_dict[x] == alien_dict[pivot]:
                equal += [x]
            else:
                right += [x]
        return alien_qsort(left) + equal + alien_qsort(right)

case_size = int(input())
for case in range(1, case_size + 1):
    N = input()
    alien_list = list(input().split())
    print(f'#{case}')
    print(' '.join(alien_qsort(alien_list)))
