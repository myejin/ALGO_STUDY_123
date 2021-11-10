"""
Title : 자연수 색칠하기
Link : https://www.acmicpc.net/problem/23048
"""

N = int(input())
colors = [0] * N
colors[0] = 1

color_now = 2
for i in range(2, N + 1):
    if not colors[i - 1]:
        colors[i - 1] = color_now
        for j in range(i * 2, N + 1, i):
            if not colors[j - 1]:
                colors[j - 1] = color_now
        color_now += 1

print(color_now - 1)
print(*colors)
