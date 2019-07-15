# bill_a: P, bill_b: Q, standard_b: R, additional: S, water: W

# A사 요금: P * W
# B사 요금 - R 이하: Q
# B사 요금 - R 이상: Q + S * (W - R)

def comparison_bill(bill_a, bill_b, standard_b, additional, water):
    total_a = bill_a * water
    if water <= standard_b:
        total_b = bill_b
    else:
        total_b = bill_b + (additional * (water - standard_b))

    if total_a > total_b:
        return total_b
    else:
        return total_a


case_size = int(input())
result_list = []
try:
    for number in range(case_size):
        P, Q, R, S, W = map(int, input().split())
        if 1 <= P and Q and R and S and W <= 10000:
            result_list += [comparison_bill(P, Q, R, S, W)]
        else:
            raise ValueError
    for key, value in enumerate(result_list):
        print("#{0} {1}".format(key + 1, value))

except ValueError:
    print("올바른 범위의 수를 입력해주세요")
