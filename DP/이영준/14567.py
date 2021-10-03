"""
Title : 선수과목 (Prerequisite)
Link : https://www.acmicpc.net/problem/14567
"""

import sys, collections
input = sys.stdin.readline

n, m = map(int, input().split())
# 후행 과목 리스트
post = [[] for _ in range(n + 1)]
# 선수 과목이 몇개인지
pre = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    post[a].append(b)
    pre[b] += 1

# 정답 / 기본은 한학기
ans = [1] * (n + 1)

# 선수 과목 없는 경우
queue = collections.deque([])
for i in range(1, n + 1):
    if not pre[i]:
        queue.append(i)
while queue:
    sub = queue.popleft()
    for p in post[sub]:
        # 각 후행 과목에 대해 선수 과목 수 - 1
        # 정답은 항상 이전보다 크거나 같으므로 계속 최신화
        pre[p] -= 1
        ans[p] = ans[sub] + 1
        # 선행 과목 없으면 큐 추가
        if not pre[p]:
            queue.append(p)

print(*ans[1:])
