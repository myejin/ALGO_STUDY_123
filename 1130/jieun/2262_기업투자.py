# N 투자 금액, M 투자 가능 기업수
N, M = map(int, input().split())
si = [[0]*(M+1)] + [list(map(int, input().split())) for _ in range(N)]
# 배낭 문제. 최대 금액 구하기
# 최종 정답은 dp[n][m]이 될 것 -> n만큼 투자하고, m번째 기업 까지 투자
# 최대 이익
dp = [[0]*(M+1) for _ in range(N+1)]
# 투자한 액수
inv = [[[0]*(M+1) for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        maxval = 0
        maxinv = []
        for k in range(i):
            # i만큼 투자해서 최대금액 구하기 위해서는..
            # 만약 j-1번째 기업까지 k 금액만큼을 투자했을 때, j번째 기업이 i-k 금액을 투자했을 때를 판단
            if dp[k][j-1] + si[i-k][j] > maxval:
                maxval = dp[k][j-1] + si[i-k][j]
                maxinv = inv[k][j-1][:]
                maxinv[j] = i-k
        if maxval > dp[i][j-1]:
            dp[i][j] = maxval
            inv[i][j] = maxinv[:]
        else:
            dp[i][j] = dp[i][j-1]
            inv[i][j] = inv[i][j-1][:]

for i in dp:
    print(i)

print(dp[N][M])
print(*inv[N][M][1:])