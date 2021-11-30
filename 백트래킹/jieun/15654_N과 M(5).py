n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s = []


def dfs():
    if len(s) == m:
        print(*s)
        return
    for a in arr:
        if a not in s:
            s.append(a)
            dfs()
            s.pop()


dfs()