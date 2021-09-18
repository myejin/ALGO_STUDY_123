"""
Title : 지금 밥이 문제냐
Link : https://www.acmicpc.net/problem/12787
"""

import sys
input = sys.stdin.readline


for _ in range(int(input())):
    m, n = input().strip().split()
    if m == '1':
        ans = ''
        ip = list(map(int, n.split('.')))
        for p in ip:
            ans += bin(p)[2:].zfill(8)
        print(int(ans, 2))
    else:
        ans = ''
        ip = str(bin(int(n))[2:]).zfill(64)
        for i in range(8):
            ans += str(int(ip[i * 8:(i + 1) * 8], 2))
            if i != 7:
                ans += '.'
        print(ans)
