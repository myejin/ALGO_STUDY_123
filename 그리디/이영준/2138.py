"""
Title : 전구와 스위치
Link : https://www.acmicpc.net/problem/2138
"""

import sys
input = sys.stdin.readline
IIS = lambda: list(int(i) for i in input().strip())


def switch(lights ,st, end):
    for i in range(st, end + 1):
        if lights[i]:
            lights[i] = 0
        else:
            lights[i] = 1
    return lights


n = int(input())
# 처음 스위치를 하지 않을 때, 작동할 때
before_0 = IIS()
before_1 = before_0[::]
before_1 = switch(before_1, 0, 1)
after = IIS()

count_0 = 0
count_1 = 1
for i in range(1, n):
    if before_0[i - 1] != after[i - 1]:
        if i == n - 1:
            switch(before_0, i - 1, i)
            count_0 += 1
        else:
            switch(before_0, i - 1, i + 1)
            count_0 += 1
    if before_1[i - 1] != after[i - 1]:
        if i == n - 1:
            switch(before_1, i - 1, i)
            count_1 += 1
        else:
            switch(before_1, i - 1, i + 1)
            count_1 += 1


if before_0[-1] == after[-1]:
    print(count_0)
elif before_1[-1] == after[-1]:
    print(count_1)
else:
    print(-1)
