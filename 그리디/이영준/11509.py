"""
Title : 풍선 맞추기
Link : https://www.acmicpc.net/problem/11509
"""

from collections import defaultdict
import sys
input = sys.stdin.readline


N = int(input())
seq = list(map(int, input().split()))

arrows = defaultdict(int)
arrow_count = 0

for h in seq:
    if arrows[h]:
        arrows[h] -= 1
        if h > 1:
            arrows[h - 1] += 1
    else:
        arrow_count += 1
        arrows[h - 1] += 1

print(arrow_count)
