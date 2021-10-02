import sys, collections, math

input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 행렬 곱하는 함수
def matrix_mul(x: list, y: list) -> list:
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                tmp[i][j] += x[i][k] * y[k][j]
            tmp[i][j] %= 1000
    return tmp

# 행렬의 2 ^ i 제곱의 저장
matrix = collections.defaultdict(list)
# 현재 제곱
order = 1
matrix[1] = a
result = a

while True:
    if order == b:
        break
    if order * 2 <= b:
        result = matrix_mul(result, result)
        order *= 2
        matrix[order] = result
    elif order * 2 > b:
        dif = b - order
        dif = int(math.log2(dif))
        order += 2 ** dif
        result = matrix_mul(result, matrix[2 ** dif])

for i in range(n):
    for j in range(n):
        print(result[i][j] % 1000, end = ' ')
    print()
