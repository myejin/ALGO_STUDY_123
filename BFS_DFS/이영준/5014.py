"""
Title : 스타트링크
Link : https://www.acmicpc.net/problem/5014
"""

import collections


def bfs(f, s, g, u, d):
    queue = collections.deque([(s, 0)])
    floor_visited = [False] * (f + 1)
    floor_visited[s] = True
    while queue:
        now, count = queue.popleft()
        if now == g:
            return count
        up = now + u
        down = now - d
        if up <= f and not floor_visited[up]:
            queue.append((up, count + 1))
            floor_visited[up] = True
        if down >= 1 and not floor_visited[down]:
            queue.append((down, count + 1))
            floor_visited[down] = True
    return 'use the stairs'


f, s, g, u, d = map(int, input().split())

# u 또는 d가 0인 경우
if not u and not d:
    print('use the stairs')        
elif not u and g > s:
    print('use the stairs')        
elif not d and g < s:
    print('use the stairs')        
else:
    print(bfs(f, s, g, u, d))

'''
# 메모리 초과, 조금 더 간단하게
# 해당 층 방문을 비트마스크로
import sys
sys.setrecursionlimit(10**7)


def search(now: int, target: int, count: int) -> int:
    global f, u, d, floor_visited
    # 최대 제한 층 f, 위로 u, 아래로 d층 이동
    # 목표층에 도달한 경우
    if now == target:
        return count
    # 무한 루프 확인
    if count >= 10 ** 6:
        return 'use thr stairs'
    # 위층, 아래층으로 이동
    up_floor = now + u
    down_floor = now - d
    if up_floor <= f and not floor_visited[up_floor]:
        floor_visited[up_floor] = True
        up_count = search(up_floor, target, count + 1)
    else:
        up_count = 'use thr stairs'
    if down_floor >= 1 and not floor_visited[down_floor]:
        floor_visited[down_floor] = True
        down_count = search(down_floor, target, count + 1)
    else:
        down_count = 'use thr stairs'
    
    if type(up_count) == str and type(down_count) == str:
        return 'use thr stairs'
    elif type(up_count) == str:
        return down_count
    elif type(down_count) == str:
        return up_count
    else:
        return min(up_count, down_count)



f, s, g, u, d = map(int, input().split())
floor_visited = [False] * (f + 1)

# u, d 둘 중 하나, 또는 둘 다 0인 경우
if u == 0 and d == 0:
    if s == g:
        print(0)
    else:
        print('use thr stairs')
elif u == 0 and s < g:
    print('use thr stairs')
elif d == 0 and s > g:
    print('use thr stairs')
else:
    floor_visited[s] = True
    print(search(s, g, 0))
'''