"""
Title : 호반우가 길을 건너간 이유
Link : https://www.acmicpc.net/problem/20118
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M = MIIS()
dist = N + M - 1

if dist % 2:
    print((dist - 1) * 2)
    print(f'0 0\n1 1\n0 0\n1 1')
    if N == 2:
        for j in range(2, M, 2):
            print(f'{N - 1} {j}\n{N - 1} {j + 1}\n{N - 1} {j}\n{N - 1} {j + 1}')
    elif N % 2:
        for i in range(2, N - 1, 2):
            print(f'{i} {1}\n{i + 1} {1}\n{i} {1}\n{i + 1} {1}')
        for j in range(1, M, 2):
            print(f'{N - 1} {j}\n{N - 1} {j + 1}\n{N - 1} {j}\n{N - 1} {j + 1}')
    else:
        for i in range(2, N, 2):
            print(f'{i} {1}\n{i + 1} {1}\n{i} {1}\n{i + 1} {1}')
        for j in range(2, M, 2):
            print(f'{N - 1} {j}\n{N - 1} {j + 1}\n{N - 1} {j}\n{N - 1} {j + 1}')
else:
    print(dist * 2)
    if N % 2:
        for i in range(0, N - 2, 2):
            print(f'{i} {0}\n{i + 1} {0}\n{i} {0}\n{i + 1} {0}')
        for j in range(0, M, 2):
            print(f'{N - 1} {j}\n{N - 1} {j + 1}\n{N - 1} {j}\n{N - 1} {j + 1}')
    else:
        for i in range(0, N, 2):
            print(f'{i} {0}\n{i + 1} {0}\n{i} {0}\n{i + 1} {0}')
        for j in range(1, M, 2):
            print(f'{N - 1} {j}\n{N - 1} {j + 1}\n{N - 1} {j}\n{N - 1} {j + 1}')
