N, num = input().split()
N = int(N)
dx, dy = map(int, input().split())  # 좌(-x) 우(+x) / 상(+y) 하(-y)

x, y = 0, 0
for n in range(N):
    l = 2 ** (N - n - 1)
    k = num[n]

    if k == '1':
        y += l
    elif k == '3':
        x += l
    elif k == '4':
        x += l
        y += l

a, b = x - dy, y + dx
if not (0 <= a < 2 ** N and 0 <= b < 2 ** N):
    print(-1)
else:
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
