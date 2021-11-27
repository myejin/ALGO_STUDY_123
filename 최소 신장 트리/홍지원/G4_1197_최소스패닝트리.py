# G4 1197 최소 스패닝 트리
# https://www.acmicpc.net/problem/1197
# 그래프 이론, 최소 스패닝 트리

import sys
input = sys.stdin.readline


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:                       # 부모를 더 작은 걸로 저장.
        parent[b] = a
    else:
        parent[a] = b


def find(c):     # 부모 찾기
    if parent[c] != c:    # 자기 자신이 아니라면 재귀 돌면서 부모 찾기.
        parent[c] = find(parent[c])             # 찾은 부모를 저장
    return parent[c]


V, E = map(int, input().split())
edge = list(list(map(int, input().split())) for _ in range(E))
edge.sort(key=lambda x: x[2])
parent = [i for i in range(V + 1)]   # 부모를 저장

res = 0  # 가중치
for a, b, c in edge:
    a = find(a)
    b = find(b)
    if a == b:                 # 부모가 같으면 넘기고 다르면 합치면서 가중치를 더해줌.
        continue
    union(a, b)
    res += c
print(res)

