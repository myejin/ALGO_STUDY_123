"""
Title : 박스 채우기
Link : https://www.acmicpc.net/problem/1493
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

length, width, height = MIIS()
cube = int(input())
cubes = []
for _ in range(cube):
    a, b = MIIS()
    cubes.append([2**a , b])
cubes.sort()

# 같은 크기의 정육면체 개수
target_cube_count = 0
# 정육면체로 만들지 못한 직육면체
cuboid = [(length, width, height)]

count = 0
while True:
    # 모두 채웠을 때
    if not target_cube_count and not cuboid:
        break
    # 채울 수 있는 큐브가 없을 때
    if not cubes:
        if target_cube_count:
            count = -1
        # 채우지 못한 공간이 있을 때
        if cuboid:
            for cub in cuboid:
                if all(cub):
                    count = -1
                    break
        break
    cube_size, cube_count = cubes.pop()
    # 정육면체를 8등분 하고, 채울 수 있는지 확인
    target_cube_count *= 8
    # 정육면체가 아닌 사각형들을 지금 크기로 분할
    tmp = []
    for l, w, h in cuboid:
        if l == 0 or w == 0 or h == 0:
            continue
        l_count = l // cube_size
        w_count = w // cube_size
        h_count = h // cube_size
        # 지금 크기의 큐브를 못넣는 경우
        if l_count == 0 or w_count == 0 or h_count == 0:
            tmp.append((l, w, h))
            continue
        target_cube_count += l_count * w_count * h_count
        tmp.append((l, w, h % cube_size))
        # 및면을 다 채울수 있는지 확인
        if l % cube_size == 0 and w % cube_size == 0:
            continue
        tmp.append((l % cube_size, w_count * cube_size, h_count * cube_size))
        tmp.append((l, w % cube_size, h_count * cube_size))
    cuboid = tmp
    # 확인
    if target_cube_count > cube_count:
        target_cube_count -= cube_count
        count += cube_count
    else:
        cube_count -= target_cube_count
        count += target_cube_count
        target_cube_count = 0

print(count)

'''
Counter Example
5 4 4
2
0 23
1 7
ans : -1
'''
