"""
Title : 흩날리는 시험지 속에서 내 평점이 느껴진거야
Link : https://www.acmicpc.net/problem/17951
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, K = MIIS()
    correct_counts = tuple(MIIS())
    left, right = 0, sum(correct_counts)
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        tmp = 0
        count = 0
        for correct in correct_counts:
            tmp += correct
            if tmp >= mid:
                count += 1
                tmp = 0
        if count >= K:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    print(ans)
