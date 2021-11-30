from collections import deque


n = int(input())
q = deque(range(n, 0, -1))
while len(q) > 2:
    q.pop()
    q.appendleft(q.pop())

print(q[0])