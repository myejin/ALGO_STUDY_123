"""
Title : 피보나치 수의 확장
Link : https://www.acmicpc.net/problem/1788
"""

import sys

input = sys.stdin.readline

n = int(input())

if n == 0 or n == 1:
    print(n)
    print(n)
elif n > 0:
    a, b = 0 , 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 1_000_000_000
    print(1)
    print(b)
elif n < 0:
    a, b = 1, 0
    for _ in range(-1, n - 1, -1):
        a, b = b, a - b
    if b < 0:
        print(-1)
        print(abs(b) % 1_000_000_000)
    elif b == 0:
        print(0)
        print(0)
    elif b > 0:
        print(1)
        print(abs(b) % 1_000_000_000)