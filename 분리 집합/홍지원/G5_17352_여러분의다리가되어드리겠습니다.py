# G5 17352 여러분의 다리가 되어 드리겠습니다!
# https://www.acmicpc.net/problem/17352
# 그래프 이론, 자료 구조, 그래프 탐색, 분리 집합
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


N = int(input())
parent = [i for i in range(N + 1)]   # 부모를 저장
for _ in range(N-2):
    x, y = map(int, input().split())
    union(x, y)

for i in range(1, N):              # 부모가 다 연결 안되어있을 수 있으므로 돌면서 다시 부모 찾기
    if find(i+1) != find(i):       # 부모가 갖지 않다면 print 해줌.
        print(i, i+1)
        break
