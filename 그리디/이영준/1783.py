"""
Title : 병든 나이트
Link : https://www.acmicpc.net/problem/1783
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    if m >= 8:
        print(4)
    else:
        print(1 + (m - 1) // 2)
elif m < 7:
    if m >= 5:
        print(4)
    else:
        print(m)
else:
    print(5 + (m - 7))
