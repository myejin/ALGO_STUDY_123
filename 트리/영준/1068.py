"""
Title : 트리
Link : https://www.acmicpc.net/problem/1068
"""

import sys, collections
input = sys.stdin.readline


n = int(input())
parents = list(map(int, input().split()))
node = int(input())

child = [[] for _ in range(n)]
for i in range(0, n):
    if parents[i] == -1:
        root = i
    else:
        child[parents[i]].append(i)

if root == node:
    print(0)
else:
    leaf = 0
    queue = collections.deque([root])
    
    # 모든 점 확인
    # 자식으로만 내려가므로 방문 확인 필요 없음
    while queue:
        p = queue.popleft()
        # 자식이 없으면, 잎으로 추가
        if not child[p]:
            leaf += 1
        # 자식이 하나일 때, 그 자식이 node인지 확인
        # 자식이 node만 있으면, node가 제거되 잎이 됨
        elif len(child[p]) == 1 and child[p] == [node]:
            # if p == root:
            #     continue
            leaf += 1
        else:
            # 자식노드를 확인, 제거할 노드가 아닐때만 탐색
            for q in child[p]:
                if q != node:
                    queue.append(q)
    
    print(leaf)



'''
Counter Example
5
-1 0 1 2 3
1
ans : 0
output : 1


12
1 4 3 -1 3 1 2 0 6 6 6 1
2
ans : 3
'''