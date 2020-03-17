N = int(input())
switches = list(map(int, input().split()))
M = int(input())
for i in range(M):
    gender, idx = map(int, input().split())
    if gender == 1:
        for j in range(idx - 1, N, idx):
            if switches[j] == 0:
                switches[j] = 1
            else:
                switches[j] = 0
    else:
        idx -= 1
        k = 0
        while idx - k >= 0 and idx + k < N and switches[idx-k] == switches[idx+k]:
            if switches[idx-k] == 1:
                switches[idx-k] = 0
                switches[idx+k] = 0
            else:
                switches[idx-k] = 1
                switches[idx+k] = 1
            k += 1

for i in range(0, N, 20):
    print(' '.join(map(str, switches[i:i+20])))
    