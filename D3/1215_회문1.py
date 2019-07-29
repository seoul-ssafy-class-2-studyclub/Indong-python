# manacher algorithm을 이용한 풀이
test_string = 'baaba'

def manacher_palindrome(string):
    string = '#'.join(string)
    print(string)
    N = len(string)
    radius_array = [0] * N
    r = 0
    p = 0
    for i in range(1, N-1):
        if i > r:
            radius_array[i] = 0
        else:
            i_apo = (2 * p) - i
            radius_array[i] = min(r - i, radius_array[i_apo])
        while string[i - radius_array[i]] == string[i + radius_array[i]] and i - radius_array[i] - 1 >= 0 and i + radius_array[i] + 1 < N:
            radius_array[i] += 1
        radius_array[i] -= 1
        j = i + radius_array[i]
        if j > r:
            j = r
            i = p
    return radius_array
    
print(manacher_palindrome(test_string))