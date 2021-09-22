import sys
input = sys.stdin.readline

def power(n):
    if n == 1:
        return matrix
    elif n == 2:
        return matrix_multiple(matrix, matrix)
    # 2 로 나누어지는 경우 바로 분할
    elif n % 2 == 0:
        arr = power(n//2)
        return matrix_multiple(arr, arr)
    # 2 로 나누어 나머지가 생기는 경우 나머지를 다시 곱해줌
    else:
        arr = power(n//2)
        arr2 = matrix_multiple(arr, arr)
        return matrix_multiple(arr2, matrix)

# arr1과 arr2를 곱한 값을 반환 (각 값은 1000으로 나눈 나머지로 표현)
def matrix_multiple(arr1, arr2):
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += arr1[i][k]*arr2[k][j]
            result[i][j] = result[i][j] % 1000
    return result


N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

result = power(B)

# 행렬곱이 시행되지 않아(B = 1) 나머지로 표현되지 못하는 경우를 위해 나머지로 처리
for i in range(N):
    for j in range(N):
        result[i][j] = result[i][j] % 1000

for i in result:
    print(*i)