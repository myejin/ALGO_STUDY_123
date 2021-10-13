from copy import deepcopy

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

rain_cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

for _ in range(M):
    d, s = map(int, input().split())

    # 모든 구름이 d 방향으로 s 칸 이동한다.
    for i in range(len(rain_cloud)):
        x, y = rain_cloud[i]
        x = (x + dx[d] * s) % N
        y = (y + dy[d] * s) % N
        rain_cloud[i] = (x, y)

    # 각 구름에서 비가 내린다.
    for x, y in rain_cloud:
        A[x][y] += 1

    # 복사마법
    for x, y in rain_cloud:
        for k in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx = x + k[0]
            ny = y + k[1]
            if 0 <= nx < N and 0 <= ny < N and A[nx][ny] > 0:
                A[x][y] += 1

    # 새로운 구름이 생긴다.
    new_cloud = []
    for i in range(N):
        for j in range(N):
            if (i, j) in rain_cloud:
                continue
            if A[i][j] >= 2:
                new_cloud.append((i, j))
                A[i][j] -= 2

    # 이전 구름은 사라지는게 맞다.
    rain_cloud = deepcopy(new_cloud)

ans = 0
for a in A:
    ans += sum(a)
print(ans)
