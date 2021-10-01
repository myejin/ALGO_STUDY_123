import sys
input = sys.stdin.readline

L, W, H = map(int, input().split())
N = int(input())

cube_cnt = []
for _ in range(N):
    i, cnt = map(int, input().split())
    cube_cnt.append([2 ** i, cnt])

area = 0
answer = 0
stack = [[L, W, H]]
while stack:
    l, w, h = stack.pop()
    if not (l and w and h):
        continue

    for idx in range(N - 1, -1, -1):
        x, cnt = cube_cnt[idx]

        if min(x, l, w, h) != x:
            continue
        if not cnt:
            continue

        stack.append([x, x, h - x])
        stack.append([x, h, l - x])
        stack.append([w - x, l, h])

        area += x ** 3
        answer += 1
        cube_cnt[idx][1] -= 1
        break

# print(area)
if area == L * W * H:
    print(answer)
else:
    print(-1)
