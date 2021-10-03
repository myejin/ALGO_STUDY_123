"""
Title : 평범한 배낭
Link : https://www.acmicpc.net/problem/12865
"""

import sys
input = sys.stdin.readline


n, k = map(int, input().split())

bag = [0] * (k + 1)
for _ in range(n):
    w, v = map(int, input().split())
    for i in range(k, w - 1, -1):
        bag[i] = max(bag[i - w] + v, bag[i])

print(bag[-1])
