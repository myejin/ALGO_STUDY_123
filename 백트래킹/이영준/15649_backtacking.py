"""
Title : N과 M (1)
Link : https://www.acmicpc.net/problem/15649
"""

n, m = map(int, input().split())

def dfs(per: list, used: list):
    global n, m, permutaion
    if len(per) == m:
        permutaion.append(per[::])
        return
    for k in range(1, n + 1):
        if used[k]:
            continue
        per.append(k)
        used[k] = True
        dfs(per, used)
        per.pop()
        used[k] = False

permutaion = []
dfs([], [False] * (n + 1))

for per in permutaion:
    print(*per)

