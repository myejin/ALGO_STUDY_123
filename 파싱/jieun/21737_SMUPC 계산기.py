def cal(num1, num2, op):
    if op == 'S':
        return num1 - num2
    elif op == 'M':
        return num1 * num2
    elif op == 'U':
        return num1//num2 if num1 > 0 else - (abs(num1)//num2)
    elif op == 'P':
        return num1 + num2


N = int(input())
formula = input()
answer = ''
temp = ''
opt = ''
isC = False
for c in formula:
    if c.isdigit():
        if opt :
            temp += c
        else :
            answer += c
    else :
        if opt and opt!='C' :
            answer = cal(int(answer), int(temp), opt)
            temp = ''

        if c == 'C':
            isC = True
            print(int(answer), end=' ')
        opt = c

if not isC:
    print('NO OUTPUT')