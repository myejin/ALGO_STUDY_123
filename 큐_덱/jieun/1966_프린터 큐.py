import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    imp = deque(list(map(int, input().split())))
    idx = deque([0]*n)
    idx[m] = 1
    answer = 0

    while True:
        if imp[0] == max(imp):
            answer += 1
            if idx[0] == 1:
                print(answer)
                break
            else:
                imp.popleft()
                idx.popleft()
        else :
            imp.rotate(-1)
            idx.rotate(-1)

