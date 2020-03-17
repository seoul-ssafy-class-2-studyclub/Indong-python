def btk(idx, height):
    global res
    if B <= height < res:
        res = height
    if height > res or idx == N:
        return
    btk(idx+1, height)
    btk(idx+1, height+staffs[idx])
        
for case in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    staffs = list(map(int, input().split()))
    res = 987654321
    btk(0, 0)
    print(f'#{case} {res - B}')
