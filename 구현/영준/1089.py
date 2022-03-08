"""
Title : 스타트링크 타워
Link : https://www.acmicpc.net/problem/1089
"""

import sys
input = sys.stdin.readline


def dfs(N: int, idx: int, number_now: int, possible_nums: list):
    global total_sum, numbers_count
    if idx == N:
        total_sum += number_now
        numbers_count += 1
        return
    for num in possible_nums[idx]:
        dfs(N, idx + 1, number_now * 10 + num, possible_nums)


if __name__ == '__main__':
    N = int(input())
    my_screen = [input().strip() for _ in range(5)]

    numbers = {
        1: {2, 5, 8, 11, 14},
        2: {0, 1, 2, 5, 6, 7, 8, 9, 12, 13, 14},
        3: {0, 1, 2, 5, 6, 7, 8, 11, 12, 13, 14},
        4: {0, 2, 3, 5, 6, 7, 8, 11, 14},
        5: {0, 1, 2, 3, 6, 7, 8, 11, 12, 13, 14},
        6: {0, 1, 2, 3, 6, 7, 8, 9, 11, 12, 13, 14},
        7: {0, 1, 2, 5, 8, 11, 14},
        8: {0, 1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14},
        9: {0, 1, 2, 3, 5, 6, 7, 8, 11, 12, 13, 14},
        0: {0, 1, 2, 3, 5, 6, 8, 9, 11, 12, 13, 14},
    }

    possible_nums = [[] for _ in range(N)]
    for idx in range(N):
        tmp = set()
        for r in range(5):
            for c in range(3):
                if my_screen[r][idx * 4 + c] == '#':
                    tmp.add(r * 3 + c)
        for i in range(10):
            if numbers[i] & tmp == tmp:
                possible_nums[idx].append(i)

    total_sum = 1
    num_list = []
    for idx, nums in enumerate(possible_nums):
        total_sum *= len(nums)
        sum_now = sum(nums)
        num_list.append([sum_now * 10 ** (N - idx - 1), len(nums)])
    
    if not total_sum:
        print(-1)
    else:
        ans = 0
        for num_info in num_list:
            ans += num_info[0] * total_sum // num_info[1]
        print(ans / total_sum)

'''
Counter Example
9
###...#.###.###.#.#.###.###.###.###
#.#...#...#...#.#.#.#...#.....#.#.#
#.#...#.###.###.###.###.###...#.###
#.#...#.#.....#...#...#.#.#...#.#.#
###...#.###.###...#.###.###...#.###
ans : 451458714.380952
out : 451459381.04761904
'''
