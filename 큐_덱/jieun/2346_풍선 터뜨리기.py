import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
answer = []
while True:
    idx, paper = q.popleft()
    answer.append(idx+1)

    if not q:
        break

    if paper > 0 :
        q.rotate(-(paper-1))
    else:
        q.rotate(-paper)

print(*answer)
