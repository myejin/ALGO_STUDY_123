"""
Title : 강의실 배정
Link : https://www.acmicpc.net/problem/11000
"""

import heapq
import sys
input = sys.stdin.readline


N = int(input())
classes = [tuple(map(int, input().split())) for _ in range(N)]
classes.sort(key=lambda x:x[0])

heap = [classes[0][1]]
for s, t in classes[1:]:
    if s < heap[0]:
        heapq.heappush(heap, t)
    else:
        heapq.heappushpop(heap, t)

print(len(heap))
