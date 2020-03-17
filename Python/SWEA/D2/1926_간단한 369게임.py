import re
p = re.compile('[3|6|9]')
q = re.compile('[^3|6|9]')

N = int(input())
result_list = []
if 10 <= N <= 1000:
    for i in range(1, N + 1):
        if p.search(str(i)):
            number = q.sub('', str(i))
            number = p.sub('-', number)       
            result_list.append(number)
        else:
            result_list.append(i)
result = ' '.join(map(str,result_list))
print(result)
