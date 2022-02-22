import sys
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

def Union(a, b):
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb

def Find(ch):
    if parent[ch] != ch:
        parent[ch] = Find(parent[ch])
    return parent[ch]


N, M = MIIS()
s, e = MIIS()
parent = [i for i in range(N + 1)]
bridges = [tuple(MIIS()) for _ in range(M)]
# 무게제한이 큰 순서대로 정렬
bridges.sort(key=lambda x : x[2], reverse=True)

for h1, h2, k in bridges:
    Union(h1, h2)
    # 출발과 도착이 이어지는 순간의 무게제한 출력
    if Find(s) == Find(e):
        print(k)
        break
else:
    print(0)