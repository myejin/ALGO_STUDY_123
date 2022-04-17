"""
Title : 전생했더니 슬라임 연구자였던 건에 대하여 (Hard)
Link : https://www.acmicpc.net/problem/14698
"""

import heapq
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        heap = list(map(int, input().split()))
        heapq.heapify(heap)
        ans = 1
        while len(heap) > 1:
            a, b = heapq.heappop(heap), heapq.heappop(heap)
            ans *= a * b
            heapq.heappush(heap, a * b)
        print(ans % 1_000_000_007)
