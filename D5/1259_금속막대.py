for case in range(1, int(input()) + 1):
    N = int(input())
    screws = list(map(int, input().split()))
    ad_list = [[] for i in range(max(screws) + 1)]
    for i in range(0, (N*2) - 1, 2):
        ad_list[screws[i]].append(screws[i+1])
    
    lines = []
    for i in range(len(ad_list)):
        part = []
        if ad_list[i]:
            idx = ad_list[i].pop()
            part += [i, idx]
            while ad_list[idx]:
                part.append(idx)
                idx = ad_list[idx].pop()
                part.append(idx)
        if part and not lines:
            lines.append(part)
        elif part and lines:
            for j in range(len(lines)):
                if lines[j][0] == part[-1]:
                    lines[j] = part + lines[j] 
                elif lines[j][-1] == part[0]:
                    lines[j] += part

    print(f'#{case} {" ".join(map(str, lines[0]))}')
    