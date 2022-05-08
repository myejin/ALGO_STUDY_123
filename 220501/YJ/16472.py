"""
Title : 고냥이
Link : https://www.acmicpc.net/problem/16472
"""

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    s = input().strip()
    left, right = 0, 1
    alphabets = {t: 0 for t in set(s)}
    alphabets[s[0]] += 1
    count = 1
    ans = 1
    while left <= right < len(s):
        t = s[right]
        if count < N or alphabets[t]:
            if not alphabets[t]:
                count += 1
            alphabets[t] += 1
            right += 1
            if ans < right - left:
                ans = right - left
        else:
            t = s[left]
            alphabets[t] -= 1
            if not alphabets[t]:
                count -= 1
            left += 1
    print(ans)
