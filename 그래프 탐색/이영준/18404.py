"""
Title : 현명한 나이트
Link : https://www.acmicpc.net/problem/18404
"""

import sys, collections
input = sys.stdin.readline


n, m = map(int, input().split())
x, y = map(int, input().split())

# 나이트 위치, 이동 횟수, 잡은 말의 수
queue = collections.deque([(x, y, 0)])
# -2: 미방문, -1: 방문
visited = [[-2] * (n + 1) for _ in range(n + 1)]
visited[x][y] = -1
for i in range(m):
    a, b = map(int, input().split())
    visited[a][b] = i

direction = {
    0: (-2, -1), 1: (-2, 1), 2: (-1, 2), 3: (1, 2),
    4: (2, 1), 5: (2, -1), 6: (-1, -2), 7: (1, -2)
}


count = [0] * (m)
while queue:
    if all(count):
        break
    a, b, move = queue.popleft()
    for d in range(8):
        na, nb = a + direction[d][0], b + direction[d][1]
        if 1 <= na <= n and 1 <= nb <= n:
            c = visited[na][nb]
            if c >= 0:
                count[c] = move + 1
                queue.append((na, nb, move + 1))
                visited[na][nb] = -1
            elif c == -2:
                queue.append((na, nb, move + 1))
                visited[na][nb] = -1

print(*count)
