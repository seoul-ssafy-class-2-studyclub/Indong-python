# (면의 번호, 위아래/왼쪽오른쪽, 위왼쪽/아래오른쪽)
delta = [
    [(3, 0, 0), (5, 0, 0), (2, 0, 0), (4, 0, 0)],
    [(2, 0, 2), (5, 0, 2), (3, 0, 2), (4, 0, 2)],
    [(0, 0, 2), (5, 1, 0), (1, 0, 0), (4, 1, 2)],
    [(0, 0, 0), (4, 1, 0), (1, 0, 2), (5, 1, 2)],
    [(0, 1, 0), (2, 1, 0), (1, 1, 0), (3, 1, 2)],
    [(0, 1, 2), (3, 1, 0), (1, 1, 2), (2, 1, 2)]
    ]

dis = {'U': 0, 'D': 1, 'F': 2, 'B': 3, 'L': 4, 'R': 5}

def rotate(plane, comm):
    new = []
    if comm == '+':
        for i in range(3):
            temp = [cube[plane][j][i] for j in (2, 1, 0)]
            new.append(temp)
    else:
        for i in (2, 1, 0):
            temp = [cube[plane][j][i] for j in range(3)]
            new.append(temp)
    cube[plane] = [row[:] for row in new]


def move(plane):
    d = delta[plane]
    if plane == 0 or plane == 1:
        temp = cube[4][d[3][2]][:]
        for k in range(3, 0, -1):
            for i in range(3):
                cube[d[k][0]][d[k][2]][i] = cube[d[k-1][0]][d[k-1][2]][i]
        cube[d[0][0]][d[0][2]] = temp[:]

    elif plane == 2:
        temp = []
        for k in range(2, -1, -1):
            temp.append(cube[d[3][0]][k][d[3][2]])
        for k in range(3, 0, -1):
            if k % 2:
                for i in range(3):
                    cube[d[k][0]][i][d[k][2]] = cube[d[k-1][0]][d[k-1][2]][i]
            else:
                for i in range(3):
                    cube[d[k][0]][d[k][2]][i] = cube[d[k-1][0]][-1-i][d[k-1][2]]
        cube[d[0][0]][d[0][2]] = temp[:]
    
    elif plane == 3:
        temp = []
        for k in range(3):
            temp.append(cube[d[3][0]][k][d[3][2]])
        for k in range(3, 0, -1):
            if k % 2:
                for i in range(3):
                    cube[d[k][0]][i][d[k][2]] = cube[d[k-1][0]][d[k-1][2]][-1-i]
            else:
                for i in range(3):
                    cube[d[k][0]][d[k][2]][i] = cube[d[k-1][0]][i][d[k-1][2]]
        cube[d[0][0]][d[0][2]] = temp[:]

    elif plane == 4:
        temp = []
        for k in range(2, -1, -1):
            temp.append(cube[d[3][0]][k][d[3][2]])
        for k in range(3, 0, -1):
            if k == 3:
                for i in range(3):
                    cube[d[k][0]][i][d[k][2]] = cube[d[k-1][0]][-1-i][d[k-1][2]]
            else:
                for i in range(3):
                    cube[d[k][0]][i][d[k][2]] = cube[d[k-1][0]][i][d[k-1][2]]
        for i in range(3):
            cube[d[0][0]][i][d[0][2]] = temp[i]
    
    elif plane == 5:
        temp = []
        for k in range(3):
            temp.append(cube[d[3][0]][k][d[3][2]])
        for k in range(3, 0, -1):
            if k == 3:
                for i in range(3):
                    cube[d[k][0]][i][d[k][2]] = cube[d[k-1][0]][i][d[k-1][2]]
            else:
                for i in range(3):
                    cube[d[k][0]][i][d[k][2]] = cube[d[k-1][0]][-1-i][d[k-1][2]]
        for i in range(3):
            cube[d[0][0]][i][d[0][2]] = temp[i]


for case in range(int(input())):
    cube = [
    [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
    [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
    [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
    [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
    [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
    [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
    ]
    N = int(input())
    com_list = list(input().split())
    for com in com_list:
        plane, r = list(com)
        rotate(dis[plane], r)
        move(dis[plane])
        if r == '-':
            move(dis[plane])
            move(dis[plane])
    for i in range(3):
        print(''.join(cube[0][i]))
