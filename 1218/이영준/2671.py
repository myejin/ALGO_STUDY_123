"""
Title : 잠수함식별
Link : https://www.acmicpc.net/problem/2671
"""

import sys
input = sys.stdin.readline

S = input().strip()

# find continuous zeros
pattern = []
tmp = ''
for s in S:
    if s == '1':
        if tmp == '0':
            pattern.append(tmp)
            tmp = ''
        elif len(tmp) >= 2:
            pattern.append('zero')
            tmp = ''
        pattern.append(s)
    else:
        tmp += s

# find 01 pattern
new_pattern = []
tmp_pattern = []
for pat in pattern:
    if pat == '1':
        if tmp_pattern and tmp_pattern[-1] == '0':
            tmp_pattern.pop()
            new_pattern.append(tmp_pattern[::])
            tmp_pattern = []
        else:
            tmp_pattern.append(pat)
    else:
        tmp_pattern.append(pat)
else:
    new_pattern.append(tmp_pattern)

# find 100~1~ pattern
for samll_pattern in new_pattern:
    if not samll_pattern:
        continue
    last_zero_idx = -2
    for i in range(len(samll_pattern)):
        if samll_pattern[i] == '0':
            print('NOISE')
            exit()
        if samll_pattern[i] == 'zero':
            if i - last_zero_idx <= 2:
                print('NOISE')
                exit()
            last_zero_idx = i
    else:
        if last_zero_idx == -2 or last_zero_idx == len(samll_pattern) - 1:
            print('NOISE')
            exit()
else:
    print('SUBMARINE')


'''
import re
import sys
input = sys.stdin.readline

pattern = re.compile('(100+1+|01)+')
S = input().strip()
match = pattern.fullmatch(S)
if match == None:
    print('NOISE')
else:
    if match.end() == len(S):
        print('SUBMARINE')
    else:
        print('NOISE')
'''

'''
def check(S: str) -> str:
    str_now = ''
    idx = 0
    len_S = len(S)
    while idx < len_S:
        if str_now == '':
            if S[idx] == '0':
                if idx == len_S - 1:
                    return 'NOISE'
                elif S[idx + 1] == '1':
                    idx += 2
                else:
                    return 'NOISE'
            else:
                str_now += '1'
                idx += 1
        elif str_now == '1':
            while idx < len_S:
                if S[idx] == '0':
                    str_now += '0'
                    idx += 1
                else:
                    break
            if len(str_now) < 3:
                return 'NOISE'
        else:
            while idx < len_S:
                if S[idx] == '1':
                    str_now += '1'
                    idx += 1
                else:
                    break
            if str_now[-1] == '0':
                return 'NOISE'
            str_now = ''
    return 'SUBMARINE'


S = input().strip()
print(check(S))
'''

'''
Counter Example
10011001100110010110011111111111111111111101
ans : SUBMARINE
'''