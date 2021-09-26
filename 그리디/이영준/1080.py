"""
Title : 행렬
Link : https://www.acmicpc.net/problem/1080
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def search(n: int, m: int, A: list, B: list) -> int:
    count = 0 
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            # 왼쪽 위만 확인
            if A[i - 1][j - 1] != B[i - 1][j - 1]:
                for a in range(i - 1, i + 2):
                    for b in range(j - 1, j + 2):
                        if A[a][b]:
                            A[a][b] = 0
                        else:
                            A[a][b] = 1
                # 횟수 증가
                count += 1
    if A == B:
        return count 
    else:
        return -1


n, m = MIIS()
A = [list(int(i) for i in input().strip()) for _ in range(n)]
B = [list(int(i) for i in input().strip()) for _ in range(n)]

print(search(n, m, A, B))
