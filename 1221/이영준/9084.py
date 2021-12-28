"""
Title : 동전
Link : https://www.acmicpc.net/problem/9084
"""

import sys
input = sys.stdin.readline


for _ in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    
    count = [0] * (target + 1)
    for coin in coins:
        if coin > target:
            continue
        count[coin] += 1
        for i in range(coin + 1, target + 1):
            count[i] += count[i - coin]
    print(count[-1])
