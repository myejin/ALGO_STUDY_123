"""
Title : 겹치는 선분
Link : https://www.acmicpc.net/problem/1689
"""

import heapq
import sys
input = sys.stdin.readline


def solution() -> None:
    N = int(input())
    lines = sorted(list(tuple(map(int, input().split())) for _ in range(N)))

    ans = 1
    heap = []
    for s, e in lines:
        while heap:
            if heap[0] <= s:
                heapq.heappop(heap)
            else:
                break
        heapq.heappush(heap, e)
        if ans < len(heap):
            ans = len(heap)
    print(ans)
    return None


solution()
