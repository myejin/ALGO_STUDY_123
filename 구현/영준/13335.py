"""
Title : 트럭
Link : https://www.acmicpc.net/problem/13335
"""

from collections import deque
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, W, L = MIIS()
    trucks = tuple(MIIS())
    queue = deque([0] * W)
    
    idx = 0
    weights = 0
    for time in range(1_000_000):
        if idx == N:
            for i in range(W - 1, -1, -1):
                if queue[i]:
                    print(time + i + 1)
                    break
            break
        if queue[0]:
            weights -= queue[0]
            queue[0] = 0
        queue.rotate(-1)
        if weights + trucks[idx] <= L:
            queue[-1] = trucks[idx]
            weights += trucks[idx]
            idx += 1
