"""
Title : 트리 나라 관광 가이드
Link : https://www.acmicpc.net/problem/15805
"""

import sys
input = sys.stdin.readline


K = int(input())
city = list(map(int, input().split()))
city_count = max(city) + 1

parents = list(range(city_count))
parents[city[0]] = -1

for i in range(1, K):
    before, now = city[i - 1], city[i]
    if parents[now] == now:
        parents[now] = before

print(city_count)
print(*parents)
