N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


def multiply(arr1, arr2):
    ret = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for i in range(N):
                ret[x][y] += (arr1[x][i] * arr2[i][y]) % 1000
                ret[x][y] %= 1000
    return ret


def sol(arr, b):
    if b == 1:
        for i in range(len(arr)):
            arr[i] = list(map(lambda x: x % 1000, arr[i]))
        return arr
    elif b % 2:  # 홀수
        return multiply(sol(arr, b - 1), arr)
    else:
        tmp = sol(arr, b // 2)
        return multiply(tmp, tmp)


answer = sol(A, B)
for a in answer:
    print(*a)
