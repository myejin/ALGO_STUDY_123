"""
Title : 롤케이크
Link : https://www.acmicpc.net/problem/16206
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M = MIIS()
cakes = list(MIIS())

count = 0
additional_count = 0

for cake in sorted(cakes):
    if M == 0:
        break
    if cake % 10 == 0:
        if cake // 10 - 1 <= M:
            count += cake // 10
            M -= cake // 10 - 1
        else:
            count += M
            M = 0
    else:
        additional_count += cake // 10

print(count + min(M, additional_count))
