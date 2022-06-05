"""
Title : 좋은 수
Link : https://www.acmicpc.net/problem/5624
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    seq = list(map(int, input().split()))
    num_check = [False] * 200_001
    ans = 0
    for idx, x in enumerate(seq):
        for j in range(idx):
            if num_check[x - seq[j]]:
                ans += 1
                break
        for j in range(idx + 1):
            num_check[x + seq[j]] = True
    print(ans)
