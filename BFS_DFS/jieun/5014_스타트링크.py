"""
결과 값이 나오는 경우, 아닌 경우는 flag 사용보다 함수 return 으로 이용하는 게 시간이 더 빠름
왜인지 모르겠지만 up = now + U 같이 선언하고 실행하면 시간초과가 나고 일일히 now+U를 해주는건 시간 초과가 안 난다
정말 왜인지 모르겠네...
"""

from collections import deque
import sys
input = sys.stdin.readline

def bfs(F, S, G, U, D):
    q = deque([(S, 0)])
    visited = {S}

    while q:
        now, cnt = q.popleft()
        if now == G:
            return cnt

        if now + U <= F and now + U not in visited:
            q.append((now + U, cnt + 1))
            visited.add(now + U)
        if now - D >= 1 and now - D not in visited:
            q.append((now - D, cnt + 1))
            visited.add(now - D)

    return 'use the stairs'

#총 높이 F, 위치 G, 지금 S, 위로 U층, 아래로 D층
F, S, G, U, D = map(int, input().split())
print(bfs(F, S, G, U, D))
