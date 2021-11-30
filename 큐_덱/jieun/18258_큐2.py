import sys
from collections import deque

input = sys.stdin.readline

q = deque()

n = int(input())

for _ in range(n):
    order = input().split()
    if order[0] == 'pop':
        if q :
            print(q.popleft())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    else:
        q.append(order[1])
