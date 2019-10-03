# N, M, C = map(int, input().split())
# L = N - M + 1
# board = [list(map(int, input().split())) for _ in range(N)]
# honey = [[0] * L for _ in range(N)]
# profit = [[0] * L for _ in range(N)]

# for r in range(N):
#     honey[r][0] = sum(board[r][:M])
#     profit[r][0] = sum([i ** 2 for i in board[r][:M]])
#     for c in range(1, L):
#         honey[r][c] = honey[r][c-1] - board[r][c-1] + board[r][c+M-1]
#         profit[r][c] = profit[r][c-1] - board[r][c-1] ** 2 + board[r][c+M-1] ** 2

# dp = [[[0, 0] for j in range(L)] for i in range(N)]
# res = 0
# for r in range(N):
#     for c in range(L):
#         if c - M < 0:
#             bef = dp[r-1][-1][0]
#         else:
#             bef = dp[r][c-M][0]
# 이때 생각해서 다시 짜야 함!
        if honey[r][c] <= C:
#             cur = max(profit[r][c], bef)
#             temp = bef + profit[r][c]
#         else:
#             cur = bef
#             temp = 0
#         dp[r][c] = [cur, temp]
#         if res < temp:
#             res = temp

# print(res)


# print(board)
# print('honey')
# print(honey)
# print('profit')
# print(profit)
# print('====================')
# print(dp)