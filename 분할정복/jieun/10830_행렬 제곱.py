"""
입력 받을 때부터 1000을 나눈 나머지로 받아줘야 한다.
아무래도 입력에 (1001, 1001), 1 이런게 있는 듯
"""

import sys
input = sys.stdin.readline


def power(mat, n):
    if n == 1:
        return mat
    temp = power(mat, n//2)
    multi_temp = multi(temp, temp)
    if n % 2 == 1:
        multi_temp = multi(multi_temp, mat)
    return multi_temp


def multi(mat1, mat2):
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = sum([(mat1[i][k] * mat2[k][j]) % 1000 for k in range(N)]) % 1000
    return result


N, B = map(int, input().split())
array = [list(map(lambda x: x%1000, map(int, input().split()))) for _ in range(N)]
answer = power(array, B)
for z in range(N):
    print(*answer[z])
