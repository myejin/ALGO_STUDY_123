def find_p(x):
    if p[x] != x:
        p[x] = find_p(p[x])
        return p[x]
    else:
        return x


def union(x):
    pass


n = int(input())
p = [i for i in range(n+1)]
rank = []

for _ in range(n-2):
    i1, i2 = map(int, input().split())
    p1 = find_p(i1)
    p2 = find_p(i2)
    if p1 == p2:
        continue
    p[p1] = p2

ans_island = []
for i in range(1, n+1):
    if i == p[i]:
        ans_island.append(i)

print(*ans_island)