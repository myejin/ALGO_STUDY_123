import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().strip())) for _ in range(N)]
B = [list(map(int, input().strip())) for _ in range(N)]


def change(i, j):
    global A
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            A[x][y] = (A[x][y] + 1) % 2
    return


cnt = 0
for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] == B[i][j]:
            continue
        change(i, j)
        cnt += 1
if A == B:
    print(cnt)
else:
    print(-1)
