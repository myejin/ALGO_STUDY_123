import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
parent = [0]*(N+1)
tree = {i:[] for i in range(1, N+1)}

for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque([1])

while q:
    now = q.popleft()
    for child in tree[now]:
        if parent[child] == 0 :
            parent[child] = now
            q.append(child)

print(*parent[2:])