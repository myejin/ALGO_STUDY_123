import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())
    p = []
    for _ in range(N):
        p.append(list(map(int, input().split())))

    p.sort(key=lambda x:x[0])
    cnt = 1
    min_a = p[0][1]

    for i in range(1, N):
        if p[i][1] < min_a:
            min_a = p[i][1]
            cnt += 1

    print(cnt)