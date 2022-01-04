"""
Title : 링고와 수열
Link : https://www.acmicpc.net/problem/17505
"""

import sys
input = sys.stdin.readline


N, M = map(int, input().split())

ans = [0] * N
left, right = 0, N - 1
for i in range(1, N + 1):
    if M >= right - left:
        M -= right
        ans[right] = i
        right -= 1
    else:
        ans[left] = i
        left += 1

print(*ans)
