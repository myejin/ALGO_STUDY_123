"""
Title : 게임 개발
Link : https://www.acmicpc.net/problem/1516
"""

from collections import deque
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N = int(input())
    buildings_time = []
    buildings_before = []
    buildings_next = [[] for _ in range(N)]
    queue = deque()
    ans = [0] * N
    for i in range(N):
        time, *before, _ = MIIS()
        buildings_time.append(time)
        buildings_before.append(set(before))
        for b in before:
            buildings_next[b - 1].append(i)
        if not before:
            queue.append(i)
            ans[i] = time
    
    while queue:
        b = queue.popleft()
        t = ans[b]
        for next_b in buildings_next[b]:
            buildings_before[next_b] -= {b + 1}
            next_t = buildings_time[next_b]
            if t + next_t > ans[next_b]:
                ans[next_b] = t + next_t
            if not buildings_before[next_b]:
                queue.append(next_b)
    print(*ans, sep="\n")

'''
5
10 -1
20 1 -1
30 2 -1
40 3 5 -1
100 -1

ans
10
30
60
140
100
'''
