from copy import deepcopy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())  # m 질량 / s 속력 / d 방향
    if not m:
        continue
    board[r - 1][c - 1].append((m, s, d))

for _ in range(K):
    # 모든 파이어볼이 방향 d로 속력 s만큼 이동한다.
    tmp = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                continue
            for m, s, d in board[i][j]:
                x = (i + dx[d] * s) % N
                y = (j + dy[d] * s) % N
                tmp[x][y].append((m, s, d))

    # 2개 이상의 볼이 있는 칸에서 일어나는 일
    for i in range(N):
        for j in range(N):
            if len(tmp[i][j]) <= 1:
                continue

            sum_m, sum_s, d_arr = 0, 0, []
            for m, s, d in tmp[i][j]:
                sum_m += m
                sum_s += s
                d_arr.append(d % 2)

            new_m, new_s = sum_m // 5, sum_s // len(tmp[i][j])
            tmp[i][j].clear()
            if not new_m:
                continue

            dd = []
            s = sum(d_arr)
            if not s or s == len(d_arr):
                dd = [0, 2, 4, 6]
            else:
                dd = [1, 3, 5, 7]
            for d in dd:
                tmp[i][j].append((new_m, new_s, d))

    board = deepcopy(tmp)

ans = 0
for i in range(N):
    for j in range(N):
        if not board[i][j]:
            continue
        for m, _, _ in board[i][j]:
            ans += m
print(ans)
