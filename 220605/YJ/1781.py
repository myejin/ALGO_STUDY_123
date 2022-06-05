"""
Title : 컵라면
Link : https://www.acmicpc.net/problem/1781
"""

import heapq
from sys import stdin

input = stdin.readline

if __name__ == "__main__":
    N = int(input())
    cup_ramyeon = []
    for i in range(1, N + 1):
        deadline, ramyeon = map(int, input().split())
        cup_ramyeon.append((-ramyeon, deadline))
    cup_ramyeon.sort(key=lambda x: (x[1], -x[0]))

    heap = []
    day = cup_ramyeon[-1][1]
    ans = 0
    while cup_ramyeon or heap:
        if not heap:
            day = cup_ramyeon[-1][1]
        while cup_ramyeon:
            if day <= cup_ramyeon[-1][1]:
                heapq.heappush(heap, cup_ramyeon.pop())
            else:
                break
        if heap:
            if day <= heap[0][1]:
                ans += -heap[0][0]
                day -= 1
                if not day:
                    break
            heapq.heappop(heap)
    print(ans)

"""
3
1 1
2 50
2 100
"""
