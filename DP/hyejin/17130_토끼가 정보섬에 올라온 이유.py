import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Map = []
ri, rj = 0, 0
no_exit = True
for i in range(N):
    tmp = list(input())
    Map.append(tmp)
    for j in range(M):
        if tmp[j] == 'R':
            ri, rj = i, j
        elif tmp[j] == 'O':
            no_exit = False

if no_exit:
    print(-1)
else:
    answer = []
    dp = [[-1] * M for _ in range(N)]
    dp[ri][rj] = 0
    for j in range(rj, M - 1):
        for i in range(N):
            if dp[i][j] == -1:
                continue
            for d in [0, 1, -1]:
                x = i + d
                y = j + 1
                if not (0 <= x < N):
                    continue
                if Map[x][y] == '#':
                    continue

                if Map[x][y] == 'C':
                    dp[x][y] = max(dp[x][y], dp[i][j] + 1)
                else:
                    dp[x][y] = max(dp[x][y], dp[i][j])
                    if Map[x][y] == 'O':
                        answer.append(dp[x][y])

    if not answer:
        print(-1)
    else:
        print(max(answer))
