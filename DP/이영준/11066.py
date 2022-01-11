"""
Title : 파일 합치기
Link : https://www.acmicpc.net/problem/11066
"""

from itertools import accumulate
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    N = int(input())
    pages = list(map(int, input().split()))
    prefix_pages = [0] + list(accumulate(pages))
    
    dp = [[0] * N for _ in range(N)]
    for count in range(1, N):
        for left in range(N - count):
            right = left + count
            min_memory = 10 ** 10
            for mid in range(left, right):
                memory = dp[left][mid] + dp[mid + 1][right]\
                    + (prefix_pages[mid + 1] - prefix_pages[left])\
                    + (prefix_pages[right + 1] - prefix_pages[mid + 1])
                if min_memory > memory:
                    min_memory = memory
            dp[left][right] = min_memory
    
    print(dp[0][N - 1])
