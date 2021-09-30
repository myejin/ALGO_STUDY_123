N, num = input().split()
N = int(N)
dx, dy = map(int, input().split())  # 좌(-x) 우(+x) / 상(+y) 하(-y)
a, b = 0, 0


def get_ab(x, y, idx):
    global N, num, a, b

    if idx == N:
        a, b = x, y
        return

    l = 2 ** (N - idx - 1)
    k = num[idx]

    if k == '1':
        y += l
    elif k == '3':
        x += l
    elif k == '4':
        x += l
        y += l

    get_ab(x, y, idx + 1)


def solution():
    global N, num, a, b

    get_ab(0, 0, 0)

    a, b = a - dy, b + dx
    if not (0 <= a < 2 ** N and 0 <= b < 2 ** N):
        print(-1)
        return

    answer = ''
    for n in range(N):
        l = 2 ** (N - n - 1)

        if 0 <= a < l <= b:
            answer += '1'
            b -= l
        elif 0 <= a < l and 0 <= b < l:
            answer += '2'
        elif 0 <= b < l <= a:
            answer += '3'
            a -= l
        else:
            answer += '4'
            a -= l
            b -= l

    print(answer[::])
    return


solution()
