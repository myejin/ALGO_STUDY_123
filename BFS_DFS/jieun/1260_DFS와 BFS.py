from collections import deque

n, m, v = map(int, input().split())
maps = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    maps[a][b] = 1
    maps[b][a] = 1


def dfs(v, visited):
    visited.append(v)
    for i in range(n+1):
        if maps[v][i] == 1 and (i not in visited):
            dfs(i, visited)
    return visited


def bfs(v) :
    q = deque()
    visited = [v]
    q.append(v)

    while q :
        c = q.popleft()
        for i in range(n+1):
            if maps[c][i] == 1 and (i not in visited):
                visited.append(i)
                q.append(i)
    return visited

print(*dfs(v, []))
print(*bfs(v))