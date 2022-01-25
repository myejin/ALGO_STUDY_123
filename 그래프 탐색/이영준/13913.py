"""
Title : 숨바꼭질 4
Link : https://www.acmicpc.net/problem/13913
"""

from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

visited_last = [-2] * 100_001
queue = deque([(-1, N)])
while queue:
    last, now = queue.popleft()
    if visited_last[now] != -2:
        continue
    visited_last[now] = last
    if now == M:
        break
    if now * 2 <= 100_000 and visited_last[now * 2] == -2:
        queue.append((now, now * 2))
    if now + 1 <= 100_000 and visited_last[now + 1] == -2:
        queue.append((now, now + 1))
    if now - 1 >= 0 and visited_last[now - 1] == -2:
        queue.append((now, now - 1))

route = [M]
while True:
    last = visited_last[route[-1]]
    if last == -1:
        break
    route.append(last)

print(len(route) - 1)
print(*route[::-1])
