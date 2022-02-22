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
parent = [i for i in range(N + 1)]

bridges = [tuple(MIIS()) for _ in range(M)]
# 중량제한이 높은 순으로 다리 정렬
bridges.sort(key=lambda x : x[2], reverse=True)

S, E = MIIS()

# 중량제한이 높은 다리부터 이어나감
for a, b, c in bridges:
    Union(a, b)
    # 시작과 끝이 이어지는 순간의 중량제한을 출력
    if Find(S) == Find(E):
        print(c)
        break