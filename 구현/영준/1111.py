"""
Title : IQ Test
Link : https://www.acmicpc.net/problem/1111
"""

import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))


if N <= 2:
    if seq == [seq[0]] * 2:
        print(seq[0])
    else:
        print('A')
else:
    if seq[0] == seq[1]:
        if seq == [seq[0]] * N:
            print(seq[0])
        else:
            print('B')
    else:
        a = (seq[1] - seq[2]) // (seq[0] - seq[1])
        b = seq[1] - a * seq[0]
        possible = True
        for i in range(N - 1):
            x, y = seq[i], seq[i + 1]
            if x * a + b != y:
                possible = False
                break
        print(seq[-1] * a + b if possible else 'B')
