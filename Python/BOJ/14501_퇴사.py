def resign(day):
    if dp[day] != -1:
        return dp[day]
    workday = day + (work[day][0] - 1)
    if workday > N:
        dp[day] = 0
        return 0
    pay = work[day][1]
    max_pay = pay
    for i in range(workday + 1, N + 1):
        temp = pay + resign(i)
        if temp > max_pay:
            max_pay = temp
    dp[day] = max_pay
    return max_pay

N = int(input())
dp = [-1] * (N + 1)
work = [[]]
for _ in range(N):
    work.append(list(map(int, input().split())))

result = 0
for i in range(1, N + 1):
    earnings = resign(i)
    if result < earnings:
        result = earnings

print(result)
