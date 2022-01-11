"""
Title : 행렬 곱셈 순서
Link : https://www.acmicpc.net/problem/11049
"""

import sys
input = sys.stdin.readline


N = int(input())
size = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
for count in range(1, N):
    for left in range(N - count):
        right = left + count
        min_multiples = 10 ** 10
        for mid in range(left, right):
            multiples = dp[left][mid] + dp[mid + 1][right] + size[left][0] * size[mid][1] * size[right][1]
            if min_multiples > multiples:
                min_multiples = multiples
        dp[left][right] = min_multiples

print(dp[0][N - 1])

'''
5
2 3
3 5
5 2
2 6
6 4
'''