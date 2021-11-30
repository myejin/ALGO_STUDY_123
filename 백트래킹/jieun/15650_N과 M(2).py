n, m = map(int, input().split())

s = []

def dfs(start):
    if len(s) == m:
        print(*s)
    for i in range(start, n+1):
        if i not in s:
            s.append(i)
            dfs(i)
            s.pop()

dfs(1)