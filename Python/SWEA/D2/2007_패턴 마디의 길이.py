case_size = int(input())
try:
    for case in range(case_size):
        word = input()
        if len(word) == 30:
            result = 0
            #'kakaokakaokakaokakaokakaokakaokakao' 라는 단어를 입력했다고 가정
            i = 1
            while i <= 10:
                # word[:2](ka)와 word[2:4](ka)가 같다면
                if word[:i+1] == word[i+1:i+(i+2)]:
                    count_set = set()
                    # 불필요한 단어(예를 들어 SAMSUMG의 SA)가 set에 들어가는 걸 방지하기 위해 마지막 숫자를 '전체 범위를 단어 수로 나눈 나머지'를 빼줌.
                    # 간격을 지정함으로써 단어 단위로 set에 들어갈 수 있게 한다.
                    # 'ka' 'ka' 'ok' 'ak' 'ao'가 들어감
                    for j in range(0, len(word) - (len(word) % (i + 1)), i+1):
                        count_set.add(word[j:j+i+1])
                    # set의 길이가 1 초과라면 그냥 넘김
                    if len(count_set) > 1:
                        i += 1
                    # 아니면 결과값 출력
                    else:
                        result += len(''.join(list(count_set)[0]))
                        break
                else:
                    i += 1
        else:
            raise ValueError
        print("#{0} {1}".format(case + 1, result))

except ValueError:
    print('올바른 범위의 수를 입력해주세요.')