import sys, copy
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

def set_oper(arr: list, cnt: int):
    global used, result
    if cnt >= K:
        for i in range(N):
            result = min(result, sum(arr[i]))
        return
    for i in range(K):
        if not used[i]:
            used[i] = 1
            set_oper(turn(arr, i), cnt + 1)
            used[i] = 0

# 영역을 네 부분으로 나누어서 회전 진행
def turn(arr: list, idx: int):
    new_arr = copy.deepcopy(arr)
    r, c, s = oper[idx]
    for dr in range(-s, s + 1):
        for dc in range(-s, s + 1):
            d = dr + dc
            nr, nc = r + dr - 1, c + dc - 1
            if dr < dc and d <= 0:
                new_arr[nr][nc] = arr[nr][nc - 1]
            elif dr <= dc and d > 0:
                new_arr[nr][nc] = arr[nr - 1][nc]
            elif dr > dc and d >= 0:
                new_arr[nr][nc] = arr[nr][nc + 1]
            elif dr >= dc and d < 0:
                new_arr[nr][nc] = arr[nr + 1][nc]
    return new_arr


N, M, K = MIIS()
A = [list(MIIS()) for _ in range(N)]
oper = [list(MIIS()) for _ in range(K)]
used = [0] * K
result = 10000

set_oper(A, 0)

print(result)