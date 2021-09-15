"""
Title : SMUPC 계산기
Link : https://www.acmicpc.net/problem/21737
"""

import sys
input = sys.stdin.readline


def operate(num1: int, num2: int, operation: str) -> int:
    """
    num1 operation num2 의 결과값 반환
    """
    if operation == 'S':
        return num1 - num2
    elif operation == 'M':
        return num1 * num2
    elif operation == 'U':
        if num1 >= 0:
            return num1 // num2
        else:
            num1 *= -1
            num1 //= num2
            return num1 * -1
    elif operation == 'P':
        return num1 + num2


n = int(input())
poly = input().strip()

idx = 0
# 연산자 이전에 있는 숫자
# 연산자가 나오면 num_now를 num_last로
num_last = 0
operation_last = ''
# 다음 연산자 나오기 까지
# C나오면 num_now 출력
num_now = 0
output = []

while idx < len(poly):
    if poly[idx].isalpha():
        # c이면 output에 저장
        if poly[idx] == 'C':
            if operation_last:
                num_now = operate(num_last, num_now, operation_last)
                output.append(num_now)
                operation_last = ''
            else:
                output.append(num_now)
        # 연산자를 만났고, 이전 연산자가 있을 때
        elif operation_last:
            num_last = operate(num_last, num_now, operation_last)
            num_now = 0
            operation_last = poly[idx]
        # 연산자를 만났고, 이전 연산자가 없을 때
        else:
            num_last = num_now
            num_now = 0
            operation_last = poly[idx]
    # 숫자일 때
    else:
        num_now *= 10
        num_now += int(poly[idx])
    idx += 1

if output:
    print(*output)
else:
    print('NO OUTPUT')
