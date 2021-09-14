def operate(n1, n2, op):
    ret = 0
    if op == 'S':
        ret = n1 - n2
    elif op == 'M':
        ret = n1 * n2
    elif op == 'U':
        ret = n1 // n2
        if n1 < 0:
            ret += 1
    elif op == 'P':
        ret = n1 + n2
    return str(ret)


N = int(input())
S = input()

c_exist = False
num1, num2 = '', ''
op = ''

i = 0
while i < len(S):
    s = S[i]

    if s.isdigit():
        if op:
            num2 += s
        else:
            num1 += s
    else:
        if op and op != 'C':
            num1 = operate(int(num1), int(num2), op)
            num2 = ''
        if s == 'C':
            print(int(num1), end=' ')
            c_exist = True
        op = s
    i += 1

if not c_exist:
    print('NO OUTPUT')
