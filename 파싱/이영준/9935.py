"""
Title : 문자열 폭발
Link : https://www.acmicpc.net/problem/9935
"""

import sys
input = sys.stdin.readline


def check_explode(st):
    global string, explode, string_next
    l_ex = len(explode)
    idx = st
    idx_ex = 0
    # 폭발 문자열인지 확인
    while idx_ex < l_ex:
        if idx == l:
            return False
        if string[idx] != explode[idx_ex]:
            return False
        idx_ex += 1
        if idx != l:
            idx = string_next[idx]
    string_next[st - 1] = idx
    return True


string = [0] + list(input().strip())
l = len(string)
# 문자열에서 다음을 지목하는 리스트
string_next = [i + 1 for i in range(l)]
explode = list(input().strip())

prob = []
for i in range(1, l):
    if string[i] == explode[0]:
        prob.append([i, False])

# 폭발 문자열이 될 수 있는 시작마다 확인
for i in range(len(prob) - 1, -1, -1):
    # 폭발 문자열인지 확인
    if check_explode(prob[i][0]):
        prob[i][1] = True

idx = string_next[0]
ans = ''
while idx < l:
    ans += string[idx]
    idx = string_next[idx]

if ans:
    print(ans)
else:
    print('FRULA')
