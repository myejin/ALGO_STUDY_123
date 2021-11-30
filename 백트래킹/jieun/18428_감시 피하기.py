from itertools import combinations

n = int(input())
teachers = []
blank = []
maps = []

for i in range(n):
    maps.append(list(input().split()))
    for j in range(n):
        if maps[i][j] == 'T':
            teachers.append((i, j))

        if maps[i][j] == 'X':
            blank.append((i,j))


def watch(d, a, b):
    if d == 0:
        while a < n:
            if maps[a][b] == 'S':
                return True
            if maps[a][b] == 'O':
                return False
            a += 1

    if d == 1 :
        while a >= 0:
            if maps[a][b] == 'S':
                return True
            if maps[a][b] == 'O':
                return False
            a -= 1

    if d == 2:
        while b >= 0:
            if maps[a][b] == 'S':
                return True
            if maps[a][b] == 'O':
                return False
            b -= 1

    if d == 3 :
        while b < n:
            if maps[a][b] == 'S':
                return True
            if maps[a][b] == 'O':
                return False
            b += 1

    return False


def check():
    for a, b in teachers:
        for z in range(4):
            if watch(z, a, b):
                return True
    return False


find = False

def wall():
    global find
    for t in combinations(blank, 3):
        for x, y in t:
            maps[x][y] = 'O'

        if not check():
            find = True
            return

        for x, y in t:
            maps[x][y] = 'X'


wall()

if find:
    print('YES')

else :
    print('NO')
