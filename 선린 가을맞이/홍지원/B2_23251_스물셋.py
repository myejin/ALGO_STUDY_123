# B2 23251 스물셋
# https://www.acmicpc.net/problem/23251
# 수학, 사칙연산, 애드 혹

import sys
input = sys.stdin.readline

T = int(input())
k = list(int(input()) for _ in range(T))
for i in range(T):
    print(k[i]*23)

# 23을 곱해가면 된다..
