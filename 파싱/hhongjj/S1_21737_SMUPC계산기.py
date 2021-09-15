# S1 21737 SMUPC 계산기
# https://www.acmicpc.net/problem/21737
# 구현, 문자열, 파싱

from collections import deque
N = int(input())
lst = list(input())
num = deque()         # 숫자 저장
symbol = deque()      # 기호 저장

# 문자아스키코드 값은 65~90사이.
for i in range(len(lst)):
    if 65 <= ord(lst[i]) <= 90:
        symbol.append(lst[i])
    else:
        if 48 <= ord(lst[i-1]) <= 57:  # 만약에 그 전의 값도 숫자일경우 합치기
            a = int(str(num.pop()) + lst[i])
            num.append(a)
        else:
            num.append(int(lst[i]))

run = 1
if 'C' not in symbol:
    print('NO OUTPUT')
    run = 0

b = 'b'
while symbol and run:
    a = num.popleft()
    if num:                   # 만약 숫자가 1개가 남았다면 지나감
        b = num.popleft()
    sym = symbol.popleft()
    if sym == 'S':
        res = a - b
    elif sym == 'M':
        res = a * b
    elif sym == 'U':
        if a < 0:
            res = -((-a) // b)
        else:
            res = a // b
    elif sym == 'P':
        res = a + b
    else:
        res = a
        print(res, end=' ')
        if b != 'b':   # b값에 숫자가 있다면 혹시 그다음 계산을 위해 다시 집어 넣어 준다.
            num.appendleft(b)
    num.appendleft(res)



# b값을 처리하는 과정에 있어서 자꾸 틀렸음.
# b에는 어떤 숫자를 넣든 해당될 수가 있어서 아예 문자를 넣고 해당되면 숫자로 바꿨음.