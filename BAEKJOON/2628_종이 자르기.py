W, H = map(int, input().split())
N = int(input())
width = [0, W]
height = [0, H]
for i in range(N):
    d, idx = map(int, input().split())
    if d == 0:
        height.append(idx)
    else:
        width.append(idx)
width.sort()
height.sort()

max_area = 0
for i in range(1, len(width)):
    for j in range(1, len(height)):
        area = (width[i] - width[i-1]) * (height[j] - height[j-1])
        if max_area < area:
            max_area = area

print(max_area)
