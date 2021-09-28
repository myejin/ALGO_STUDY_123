# S를 T로 바꾸는 것이 아니라 T를 S로 바꾼다.
import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

while True:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if len(s) == len(t):
        break

if s==t:
    print(1)
else:
    print(0)