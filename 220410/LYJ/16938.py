"""
Title : 캠프 준비
Link : https://www.acmicpc.net/problem/16938
"""

from itertools import combinations
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, L, R, X = MIIS()
    levels = sorted(MIIS())
    count = 0
    for i in range(2, N + 1):
        for comb in combinations(levels, i):
            if comb[-1] - comb[0] < X:
                continue
            elif L <= sum(comb) <= R:
                count += 1
    print(count)
