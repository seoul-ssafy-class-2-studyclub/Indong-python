import sys
sys.stdin = open("input.txt", "r")

# def wonjae_profit(list_price):
#     if len(list_price) == 0:
#         return 0
#     else:
#         max_price = max(list_price)
#         max_index = list_price.index(max_price)
#         profit = (max_price * len(list_price[:max_index])) - sum(list_price[:max_index])
#         del list_price[:max_index + 1]
#         return profit + wonjae_profit(list_price)


# case_size = int(input())
# list_result = []
# try:
#     for case in range(case_size):
#         trade_length = int(input())
#         prices = list(map(int, input().split()))
#         if 2 <= trade_length <= 1000000 and len(list(filter(lambda x: x>10000, prices))) < 1:
#             list_result += [wonjae_profit(prices)]
    
#     for index, value in enumerate(list_result):
#         print(f"#{index + 1} {value}")

# except ValueError:
#     print('올바른 수를 입력하세요.')

# def wonjae_profit(price_list):
#     length = len(price_list)
#     index_list = []
#     price_list.reverse()
#     for i in range(length - 1):
#         if price_list[i] > price_list[i+1]:
#             index_list += [i]
#             first_index = i
#             break
#     for j in range(first_index + 1, length - 1):
#         if price_list[index_list[-1]] < price_list[j] and price_list[j] >= price_list[j+1]:
#             index_list += [j]
#     index_list = sorted(list(map(lambda x: length - x - 1, index_list)))
#     return index_list


case_size = int(input())
list_result = []
try:
    for case in range(case_size):
        trade_length = int(input())
        prices = list(map(int, input().split()))
        if 2 <= trade_length <= 1000000 and len(list(filter(lambda x: x > 10000, prices))) < 1:
            result = 0
            index_result = wonjae_profit(prices)
            for k in len(index_result):
                if k == 0:
                    sums = prices[index_result[k] - 1] * (index_result[k])
                    minus = sum(prices[:index_result[k]])
                    result = result + sums - minus
                else:
                    sums = prices[index_result[k] - 1] * (index_result[k] - index_result[k - 1] - 1)
                    minus = sum(prices[index_result[k - 1] + 1:index_result[k]])
                    result = result + sums - minus
            print(result)

except ValueError:
    print('올바른 수를 입력하세요.')
    