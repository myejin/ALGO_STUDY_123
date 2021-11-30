n = int(input())
T, P = [0]*n, [0]*n
for i in range(n):
    T[i], P[i] = map(int, input().split())

dp = [0] * (n+1)

for i in range(n):
    if dp[i] > dp[i+1]:
        dp[i+1] = dp[i]
    if i+T[i] <= n and dp[i+T[i]] < dp[i] + P[i]:
        dp[i+T[i]] = dp[i] + P[i]

print(dp[n])