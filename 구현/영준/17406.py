"""
Title : 배열 돌리기 4
Link : https://www.acmicpc.net/problem/17406
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def dfs(count: int, prev_array: list):
    global K, rotations, min_value, check
    if count == K:
        possible_min_value = calc_min_value(prev_array)
        if min_value > possible_min_value:
            min_value = possible_min_value
        return
    for i in range(K):
        if not check[i]:
            check[i] = True
            dfs(count + 1, rotate(prev_array, rotations[i]))
            check[i] = False



def rotate(prev_array: list, rotation: tuple) -> list:
    new_array = [line[::] for line in prev_array]
    r, c, s = rotation
    r, c = r - 1, c - 1
    for k in range(1, s + 1):
        for i in range(r - k, r + k):
            new_array[i][c - k] = prev_array[i + 1][c - k]
        for j in range(c - k, c + k):
            new_array[r + k][j] = prev_array[r + k][j + 1]
        for i in range(r + k, r - k, -1):
            new_array[i][c + k] = prev_array[i - 1][c + k]
        for j in range(c + k, c - k, -1):
            new_array[r - k][j] = prev_array[r - k][j - 1]
    return new_array


def calc_min_value(array):
    return min([sum(line) for line in array])


N, M, K = MIIS()
array = [list(MIIS()) for _ in range(N)]

rotations = [tuple(MIIS()) for _ in range(K)]
min_value = 10 ** 4
check = [False] * K
dfs(0, array)
print(min_value)


'''
# pypy accept
# python TLE
from copy import deepcopy
from itertools import permutations
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def rotate(prev_array: list, rotation: tuple) -> list:
    new_array = deepcopy(prev_array)
    r, c, s = rotation
    r, c = r - 1, c - 1
    for k in range(1, s + 1):
        for i in range(r - k, r + k):
            new_array[i][c - k] = prev_array[i + 1][c - k]
        for j in range(c - k, c + k):
            new_array[r + k][j] = prev_array[r + k][j + 1]
        for i in range(r + k, r - k, -1):
            new_array[i][c + k] = prev_array[i - 1][c + k]
        for j in range(c + k, c - k, -1):
            new_array[r - k][j] = prev_array[r - k][j - 1]
    return new_array


N, M, K = MIIS()
array = [list(MIIS()) for _ in range(N)]

min_value = 10 ** 4
rotations = [tuple(MIIS()) for _ in range(K)]
for permutation in list(permutations(rotations, K)):
    new_array = deepcopy(array)
    for perm in permutation:
        new_array = rotate(new_array, perm)
    possible_min_value = min([sum(line) for line in new_array])
    if min_value > possible_min_value:
        min_value = possible_min_value
print(min_value)
'''
