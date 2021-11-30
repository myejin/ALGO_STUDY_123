import sys
from collections import deque

input = sys.stdin.readline
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
clouds = deque([(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)])


def move_clouds(fd, fs, old_clouds):
    new_clouds = deque()
    for cloud in old_clouds:
        new_clouds.append(((cloud[0] + dy[fd-1] * fs) % n, (cloud[1] + dx[fd-1] * fs) % n))
    return new_clouds


def fall_rain(rain_cloud):
    for y, x in rain_cloud:
        maps[y][x] += 1


def copy_water(water_clouds):
    for y, x in water_clouds:
        add_water = 0
        for ky, kx in [(-1,-1), (1, 1), (1, -1), (-1, 1)]:
            ny = ky + y
            nx = kx + x
            if 0 <= ny < n and 0 <= nx < n and maps[ny][nx]:
                add_water += 1
        maps[y][x] += add_water


def make_clouds(old_clouds):
    new_clouds = deque()
    for i in range(n):
        for j in range(n):
            if maps[i][j] >= 2 and (i, j) not in old_clouds:
                maps[i][j] -= 2
                new_clouds.append((i, j))
    return new_clouds


def solve():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if maps[i][j]:
                cnt += maps[i][j]
    return cnt


for _ in range(m):
    d, s = map(int, input().split())
    clouds = move_clouds(d, s, clouds)
    fall_rain(clouds)
    copy_water(clouds)
    clouds = make_clouds(clouds)


print(solve())
