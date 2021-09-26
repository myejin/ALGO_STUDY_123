"""
Title : 수 묶기
Link : https://www.acmicpc.net/problem/1744
"""

import sys
input = sys.stdin.readline

negative = []
positive = []
zero = 0

for _ in range(int(input())):
    m = int(input())
    if m == 0:
        zero += 1
    elif m > 0:
        positive.append(m)
    else:
        negative.append(m)

positive.sort()
negative.sort(key=lambda x:-x)

ans = 0
while positive:
    if len(positive) >= 2:
        a, b = positive.pop(), positive.pop()
        if a == 1 or b == 1:
            ans += a + b
        else:
            ans += a * b
    elif len(positive) == 1:
        ans += positive.pop()

while negative:
    if len(negative) >= 2:
        a, b = negative.pop(), negative.pop()
        ans += a * b
    elif len(negative) == 1:
        if zero:
            negative.pop()
        else:
            ans += negative.pop()

print(ans)
