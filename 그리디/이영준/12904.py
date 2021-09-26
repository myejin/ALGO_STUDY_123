"""
Title : A와 B
Link : https://www.acmicpc.net/problem/12904
"""

import sys, collections
input = sys.stdin.readline


def search(s, t):
    s = collections.deque(list(s))
    t = collections.deque(list(t))
    now = 'r'
    while len(t) >= len(s):
        if len(s) == len(t):
            # 순서대로
            if now == 'r' and s == t:
                return 1
            # 반대로
            for i in range(len(t)):
                if s[i] != t[len(t) -1 -i]:
                    return 0
            else:
                return 1
        # now위치의 A모두 제거
        # now위치에서 B가 나오면 제거하고 now 반대로
        if now == 'l':
            if t[0] == 'A':
                t.popleft()
            elif t[0] == 'B':
                t.popleft()
                now = 'r'
        else:
            if t[-1] == 'A':
                t.pop()
            elif t[-1] == 'B':
                t.pop()
                now = 'l'
    return 0

s = input().strip()
t = input().strip()

print(search(s, t))
