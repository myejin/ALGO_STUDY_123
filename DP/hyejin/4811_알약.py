dp = [{}, {1: 1}]

for _ in range(29):
    d = {}
    for k, v in dp[-1].items():
        for x in range(1, k + 2):
            d[x] = d.get(x, 0) + v
    dp.append(d)

while True:
    N = int(input())
    if not N:
        break
    print(sum(dp[N].values()))
