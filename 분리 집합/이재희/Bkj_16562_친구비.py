import sys
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

def Union(a, b):
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        if pa < pb:
            parent[pb] = pa
            # 적은 비용으로 반영
            friend_fee[pa] = min(friend_fee[pa], friend_fee[pb])
        else:
            parent[pa] = pb
            friend_fee[pb] = min(friend_fee[pa], friend_fee[pb])

def Find(ch):
    if parent[ch] != ch:
        parent[ch] = Find(parent[ch])
    return parent[ch]


N, M, K = MIIS()
friend_fee = [0] + list(MIIS())
parent = [i for i in range(N + 1)]
total_fee = 0

for _ in range(M):
    v, w = MIIS()
    Union(v, w)

# 집합의 root 비용만 합산
for i in range(1, N + 1):
    if parent[i] == i:
        total_fee += friend_fee[i]

if total_fee > K:
    print('Oh no')
else:
    print(total_fee)