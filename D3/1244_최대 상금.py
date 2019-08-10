# 피보나치 수열을 구할 때처럼 top - bottom으로 접근하지 않고, bottom - top으로 재귀함수를 구성한다.
# cnt가 0일 때(아무 숫자도 바꾸지 않았을 때)부터 시작해 total번(우리가 찾고자 하는 목표)까지 cnt를 올려나가며
# 완전 탐색을 실시한다. 

def prize(m, total, cnt=0):
    global DP
    money = int(''.join(m))
    
    # 만약 인자로 들어온 값보다 기존에 저장되어 있는 최댓값(cnt만큼 교환했을 때의 최댓값)이 크다면 
    # False를 반환하고 분기를 끝낸다.
    # DP[cnt]보다 작은 값은 검사를 실시하지 않음으로써 탐색하는 경우의 수를 줄일 수 있게 된다.
    # 하지만 만약 DP[cnt]보다 작아 걸러지게 되는 분기 중에 최댓값이 있다면...?
    # 이론적으로 생각했을 때 오류의 여지가 존재한다.
    if DP[cnt] > money:
        return False

    # money가 더 크다면 최댓값을 갱신.
    DP[cnt] = money
    
    # cnt가 total과 같다면 우리가 원하는 만큼 교환을 한 것이므로, True를 반환하고 그 분기를 종료한다.
    # 여기서 True는 분기를 끝내는 탈출 조건의 의미만을 지니고 있다.
    # 우리가 정말로 구하고자 하는 값은 함수 밖에 있는 DP에 저장되고 있으니 특별한 값을 되돌려 줄 필요가 없다.
    if cnt == total:
        return True

    # 모든 자릿수를 교환하며 완전 탐색을 한다.
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            swap = m[:]
            swap[i], swap[j] = swap[j], swap[i]
            # 한 번 바꿨으니 cnt에 1을 더해 반복한다.
            prize(swap, total, cnt + 1)


for case in range(1, int(input()) + 1):
    M, C = input().split()
    M = [i for i in M]
    C = int(C)
    # 'n번 바꿨을 때 가장 큰 값'이 저장될 리스트를 생성한다.
    DP = [0] * (C + 1)
    prize(M, C)
    print(f'#{case} {DP[-1]}')
