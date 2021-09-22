import sys
input = sys.stdin.readline

n = int(input())
paper = [[0]*100 for _ in range(100)]

# 색종이가 붙어있는 영역은 1 로 변경
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[y+i][x+j] = 1

# 1 이 연속해서 이어지는 높이를 누적 합으로 표현
for j in range(100):
    for i in range(100):
        if paper[i][j] == 1:
            if i != 0:
                paper[i][j] = paper[i-1][j] + 1

result = 0

# 도화지를 가로 방향으로 탐색
for i in range(100):
    for j_s in range(100):
        min_len = 100
        # j_s 에서 j 까지를 한 변으로 가지는 직사각형을 탐색
        for j in range(j_s, 100):
            if paper[i][j]:
                min_len = min(min_len, paper[i][j])
                area = (j - j_s + 1) * min_len
                result = max(result, area)
            else:
                break

print(result)