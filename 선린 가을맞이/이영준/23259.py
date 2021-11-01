"""
Title : Celebrity
Link : https://www.acmicpc.net/problem/23259
"""

from itertools import permutations
import sys
input = sys.stdin.readline


def star_to_num(star: list) -> int:
    star_now = 0
    for a, b in star:
        if a > b:
            a, b = b, a
        star_now |= 1 << pair_to_num(a, b)
    return star_now


def pair_to_num(a: int, b: int) -> int:
    # 두 점 쌍 a, b로 지정할 수 있는 숫자로 변경
    # a, b 값에 따라 지정 0 ~ 9
    if a == 0:
        return b - 1
    elif a == 1:
        return b + 2
    elif a == 2:
        return b + 4
    elif a == 3:
        return b + 5


n = int(input())
check = [0] * 1024
perms = list(permutations(range(5), 5))
for _ in range(n):
    m = int(input())
    star = []
    for _ in range(m):
        a, b = map(int, input().split())
        star.append((a - 1, b - 1))
    star_num = star_to_num(star)
    if check[star_num] == 2:
        continue
    # star의 쌍을 회전하면서 다른 대응 가능 숫자 확인
    unique = True
    similar_star_nums = []
    # 점 교환 가능한 모든 위치 확인
    for perm in perms:
        similar_star = []
        # 점 회전
        for a, b in star:
            similar_star.append((perm[a], perm[b]))
        similar_star_num = star_to_num(similar_star)
        if check[similar_star_num]:
            unique = False
        similar_star_nums.append(similar_star_num)
    # 지금 점이 유일한지
    if unique:
        check[star_num] = 1
    else:
        for similar_star_num in similar_star_nums:
            check[similar_star_num] = 2

beautiful_stars_count = check.count(1)

print(beautiful_stars_count)
