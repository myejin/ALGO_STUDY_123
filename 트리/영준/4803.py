"""
Title : 트리
Link : https://www.acmicpc.net/problem/4803
"""

import sys, collections
input = sys.stdin.readline


def bfs(i: int) -> bool:
    global visited, edges
    queue = collections.deque([i])
    is_tree = True
    parent = [0] * (n + 1)
    parent[i] = i
    while queue:
        p = queue.popleft()
        for q in edges[p]:
            if p == q:
                is_tree = False
                continue
            elif visited[q] and q != parent[p]:
                is_tree = False
                continue
            elif visited[q]:
                continue
            visited[q] = True
            parent[q] = p
            queue.append(q)
    if is_tree:
        return True
    else:
        return False


tc = 0
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    tc += 1
    edges = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        edges[x].append(y)
        edges[y].append(x)
    
    tree = 0
    visited = [False] * (n + 1)
    
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            if bfs(i):
                tree += 1
    
    if not tree:
        print(f'Case {tc}: No trees.')
    elif tree == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {tree} trees.')


"""
Counter Example
3 3
1 1
1 2
2 3
ans : No trees

4 3
1 2
2 3
4 4
ans : one tree
"""
