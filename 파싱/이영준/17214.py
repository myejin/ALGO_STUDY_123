"""
Title : 다항 함수의 적분
Link : https://www.acmicpc.net/problem/17214
"""

import sys
input = sys.stdin.readline


eq = str(input().strip())
eq_integral = ''

if eq[0] == '-':
    minus = True
    eq = eq[1:]
else:
    minus = False

for i in range(len(eq)):
    if eq[i] == 'x':
        coefficient_of_x = int(eq[:i])
        idx = i + 1
        
        coefficient_of_x //= 2
        if coefficient_of_x != 1:
            eq_integral += str(coefficient_of_x) + 'x' * 2
        else:
            eq_integral += 'x' * 2

        if idx < len(eq):
            eq_integral += eq[idx]
        break
else:
    idx = 0

# 상수항 확인
if eq_integral != '':
    idx += 1
if idx < len(eq):
    constant = eq[idx:]
    if constant == '0':
        pass
    elif constant == '1':
        eq_integral += 'x'
    else:
        eq_integral += constant + 'x'


if minus:
    eq_integral = '-' + eq_integral

if eq == '0':
    eq_integral = 'W'
else:
    if eq_integral[-1] == '+':
        eq_integral += 'W'
    else:
        eq_integral += '+W'


print(eq_integral)