# 전달된 인자 x가 소수인지를 판단하는 함수
def prime_num(x):
    switch = 1  # 기본 스위치를 1로 설정
    if x != 1:
        for i in range(2, x):
            if x % i == 0:    # 0으로 나누어 떨어지는 수가 있다면(= 소수가 아니라면)
                switch = 0    # 스위치를 끄고
                return False  # False를 반환
        if switch == 1:
            return True  # 스위치가 켜져 있다면 True를 반환
    else:
        return False  # x가 1이라면 False를 반환


# 전달된 인자 x를 소인수분해 하는 함수
def prime_num_list(x):
    # x 이하의 모든 소수를 구해 리스트로 반환합니다.
    all_prime_list = [number for number in range(2, x + 1) if prime_num(number)]
    result_dict = {}
    for prime in all_prime_list:
        count = 0
        # 구한 소수 리스트에서 반복문을 실시.
        # x가 소수에 나누어 떨어진다면 count에 1을 추가하고 나눔, 더이상 나누어 떨어지지 않을 때까지 반복.
        while x % prime == 0:
            count += 1
            x //= prime
        # 결과값을 보여주는 딕셔너리에 저장
        result_dict.update({prime: count})
        # 계속 나누어져 x가 1이 되었다면 while문을 끝냅니다.
        if x == 1:
            break
    # 딕셔너리는 순서가 존재하지 않기 때문에 순서가 존재하는 리스트로 변환.
    # key=lambda x: x[0]은 result_dict.items()의 key값을 기준으로 정렬한다는 뜻입니당.
    sorted_result_list = sorted(result_dict.items(), key=lambda x: x[0])
    return sorted_result_list


# 위 함수들로 소인수분해 하여 처리할 시 수가 커질수록 처리 시간이 지나치게 상승해 문제 조건에 맞게만 수정합니다ㅜㅜ
def five_prime(x):
    prime_list = [2, 3, 5, 7, 11]
    result_dict = {}
    for prime in prime_list:
        count = 0
        while x % prime == 0:
            count += 1
            x //= prime
        result_dict.update({prime: count})

    sorted_result_list = sorted(result_dict.items(), key=lambda x: x[0])
    return sorted_result_list


case_size = int(input())
result_list = []
try:
    for number in range(case_size):
        input_number = int(input())
        if 2 <= input_number <= 10000000:
            input_prime = five_prime(input_number)
            result = "#{0}".format(number + 1)
            for j in range(len(input_prime)):
                result += " {}".format(input_prime[j][1])
            result_list += [result]
        # 입력한 숫자가 범위 밖일 경우 예외를 발생시킵니다.
        else:
            raise ValueError
    for k in result_list:
        print(k)
except ValueError:
    print("범위 내의 수를 입력해주세요.")
    