import sys
input = sys.stdin.readline


def flip(y, x):
    for r in range(y, y+3):
        for c in range(x, x+3):
            origin[r][c] = 1 - origin[r][c]


def check():
    for r in range(n):
        for c in range(m):
            if origin[r][c] != change[r][c]:
                return False
    return True


n, m = map(int, input().split())
origin = [list(map(int, list(input().rstrip()))) for _ in range(n)]
change = [list(map(int, list(input().rstrip()))) for _ in range(n)]

answer = 0

for i in range(0, n-2):
    for j in range(0, m-2):
        if origin[i][j] != change[i][j]:
            answer += 1
            flip(i, j)

if check():
    print(answer)
else:
    print(-1)