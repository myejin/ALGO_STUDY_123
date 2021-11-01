"""
Title : 블록
Link : https://www.acmicpc.net/problem/23252
"""

import sys
input = sys.stdin.readline


for _ in range(int(input())):
    A, B, C = map(int, input().split())
    # C가 A보다 많다면 불가능
    if A < C:
        print('No')
    else:
        # B가 홀수개일 때
        if B % 2:
            if C >= 1 and not (A - C) % 2:
                print('Yes')
            elif C == 0 and A >= 2 and not A  % 2:
                print('Yes')
            else:
                print('No')
        # B가 짝수개일 때
        else:
            if (A - C) % 2:
                print('No')
            else:
                print('Yes')
