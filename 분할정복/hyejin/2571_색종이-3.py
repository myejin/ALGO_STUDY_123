N = int(input())  # 색종이의 수, 100 이하
Map = [[0] * 101 for _ in range(101)]

# 10,000
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            Map[x + i][y + j] = 1

# 10,000
for i in range(1, 101):
    for j in range(100):
        if not Map[i][j]:
            continue
        Map[i][j] += Map[i - 1][j]

# 1,000,000
ans = 0
for x in range(100):
    for y1 in range(100):
        height = 100
        for y2 in range(y1, 100):
            height = min(height, Map[x][y2])
            if not height:
                break
            ans = max(ans, height * (y2 - y1 + 1))
print(ans)
