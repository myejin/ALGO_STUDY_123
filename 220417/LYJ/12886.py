"""
Title : 돌 그룹
Link : https://www.acmicpc.net/problem/12886
"""

from collections import deque
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    A, B, C = sorted(map(int, input().split()))
    total = A + B + C
    check = [[False] * (total + 1) for _ in range(total + 1)]
    ans = 0
    queue = deque([(min(A, B, C), max(A, B, C))])
    while queue:
        a, b = queue.popleft()
        if a == b == total - (a + b):
            ans = 1
            break
        for x, y in (a, b), (a, total - (a + b)), (b, total - (a + b)):
            if x < y:
                y -= x
                x += x
            elif x > y:
                x -= y
                y += y
            else:
                continue
            z = total - (x + y)
            n, m = min(x, y, z), max(x, y, z)
            if not check[n][m]:
                queue.append((n, m))
                check[n][m] = True
    print(ans)
