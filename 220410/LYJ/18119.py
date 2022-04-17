"""
Title : 단어 암기
Link : https://www.acmicpc.net/problem/18119
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    words = []
    for _ in range(N):
        tmp = 0
        for s in input().strip():
            tmp |= 1 << (ord(s) - 97)
        words.append(tmp)
    alphabets_now = (1 << 26) - 1
    ans = ''
    for _ in range(M):
        cmd, s = input().strip().split()
        alphabet = ord(s) - 97
        if cmd == '1':
            alphabets_now &= ~(1 << alphabet)
        else:
            alphabets_now |= 1 << alphabet
        ans += f"{sum([1 for word in words if (alphabets_now & word == word)])}\n"
    print(ans)
