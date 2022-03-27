"""
Title : 피자 굽기
Link : https://www.acmicpc.net/problem/1756
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    D, N = MIIS()
    oven_diameters = list(MIIS())
    pizza_diameters = list(MIIS())
    
    min_oven_diameters = oven_diameters[::]
    for i in range(1, D):
        if min_oven_diameters[i] > min_oven_diameters[i - 1]:
            min_oven_diameters[i] = min_oven_diameters[i - 1]
    
    oven_idx = D
    for pizza in pizza_diameters:
        oven_idx -= 1
        while oven_idx >= 0:
            if min_oven_diameters[oven_idx] >= pizza:
                break
            oven_idx -= 1
        if oven_idx == -1:
            break
    if oven_idx == -1:
        print(0)
    else:
        print(oven_idx + 1)
