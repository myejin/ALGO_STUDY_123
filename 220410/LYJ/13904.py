"""
Title : 과제
Link : https://www.acmicpc.net/problem/13904
"""

import heapq
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    expirations = sorted([tuple(map(int, input().split())) for _ in range(N)], reverse=True)
    heap = []
    ans = idx = 0
    time = expirations[0][0]
    while idx < N:
        while idx < N:
            if expirations[idx][0] == time:
                heapq.heappush(heap, -expirations[idx][1])
                idx += 1
            else:
                break
        if idx == N:
            next_time = 0
        else:
            next_time = expirations[idx][0]
        for _ in range(time - next_time):
            if not heap:
                break
            ans += -heapq.heappop(heap)
        time = next_time
    print(ans)
