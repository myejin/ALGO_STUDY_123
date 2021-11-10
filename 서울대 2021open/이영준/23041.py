"""
Title : 뛰는 기물
Link : https://www.acmicpc.net/problem/23041
"""

import sys
input = sys.stdin.readline


def find_gcd(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x


n, m = map(int, input().split())
# n이 더 크거나 같게
if m > n:
    n, m = m, n

g = find_gcd(n, m)
if (n // g + m // g) % 2:
    print(g * g)
else:
    print(2 * g * g)


# 서로소 >> (n + m)이 홀수 >> 1
#                     짝수 >> 2

# 서로소가 아니라면 ?
# (1, 2) 일 때와 (2, 4)일 때  다르다
# 1 >> 4
