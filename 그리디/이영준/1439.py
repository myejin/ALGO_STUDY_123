"""
Title : 뒤집기
Link : https://www.acmicpc.net/problem/1439
"""

import sys
input = sys.stdin.readline

s = list(input().strip())

count_0 = 0
count_1 = 0

st = 0
st_num = s[0]

for i in range(1, len(s)):
    if s[i] == st_num:
        continue
    else:
        if st_num == '0':
            count_0 += 1
        else:
            count_1 += 1
        st = i
        st_num = s[i]
else:
    if st_num == '0':
        count_0 += 1
    else:
        count_1 += 1

print(min(count_0, count_1))