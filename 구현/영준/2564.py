"""
Title : 경비원
Link : https://www.acmicpc.net/problem/2564
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int ,input().split())


if __name__ == '__main__':
    width, height = MIIS()
    shops = [tuple(MIIS()) for _ in range(int(input()))]

    d, pos = MIIS()
    points = [0] * 4
    if d == 1:
        points[0] = pos
        points[1] = width - pos
        points[3] = points[0] + height
        points[2] = points[1] + height
    elif d == 2:
        points[3] = pos
        points[2] = width - pos
        points[0] = points[3] + height
        points[1] = points[2] + height
    elif d == 3:
        points[0] = pos
        points[3] = height - pos
        points[1] = points[0] + width
        points[2] = points[3] + width
    else:
        points[1] = pos
        points[2] = height - pos
        points[0] = points[1] + width
        points[3] = points[2] + width

    ans = 0
    pos_check = {
        1: (0, 1),
        2: (3, 2),
        3: (0, 3),
        4: (1, 2),
    }
    for d0, pos0 in shops:
        if d == d0:
            ans += abs(pos - pos0)
        else:
            x1, x2 = pos_check[d0]
            y1, y2 = points[x1], points[x2]
            y1 += pos0
            y2 += width - pos0 if d0 in (1, 2) else height - pos0
            if y1 > y2:
                ans += y2
            else:
                ans += y1
    print(ans)
