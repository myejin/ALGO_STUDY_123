"""
Title : 문자열 잘라내기
Link : https://www.acmicpc.net/problem/2866
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    R, C = map(int, input().split())
    strings = [input().strip() for _ in range(R)]
    strings = list(zip(*strings))
    top, bottom = 0, C - 1
    ans = 0
    while top <= bottom:
        mid = (top + bottom) // 2
        words = set()
        for j in range(C):
            word = ''.join(strings[j][mid:])
            if word in words:
                break
            words.add(word)
        else:
            ans = mid
            top = mid + 1
            continue
        bottom = mid - 1
    print(ans)
