import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 1000 / 500,000
dp = [1] * (N + 1)

relations = {i:[] for i in range(1, N + 1)}
for _ in range(M):
    A, B = map(int, input().split())
    relations[B].append(A)
    dp[B] = 0

for i in range(1, N + 1):  # (1000)
    if relations[i]:
        value = 0
        for x in relations[i]:  # 다 합쳐서 500,000
            if not dp[x]:
                break
            else:
                value = max(value, dp[x])
        else:
            dp[i] = value + 1

print(*dp[1:])
