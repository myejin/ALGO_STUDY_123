import sys
input = sys.stdin.readline


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(a, b):
    fa, fb = find(a), find(b)
    p[fb] = fa


N = int(input())
p = [i for i in range(N + 1)]
for _ in range(N - 2):
    a, b = map(int, input().split())
    union(a, b)

answer = []
for i in range(1, N + 1):
    if p[i] == i:
        answer.append(i)
    if len(answer) == 2:
        break
print(*answer)
