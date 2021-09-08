"""
Title : N과 M (2)
Link : https://www.acmicpc.net/problem/15650
"""

n, m = map(int, input().split())

def dfs(comb: list, now: int):
    global n, m
    if len(comb) == m:
        print(*comb)
        return
    for i in range(now + 1, n + 1):
        comb.append(i)
        dfs(comb, i)
        comb.pop()

dfs([], 0)