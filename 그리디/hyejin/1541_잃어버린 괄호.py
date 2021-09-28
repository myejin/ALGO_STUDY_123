inp = input()
expression = []
num = ''
for i in inp:
    if i.isdigit():
        num += i
    else:
        expression.append(int(num))
        expression.append(i)
        num = ''
expression.append(int(num))

minus_check = False
answer = expression[0]
for i in range(1, len(expression)):
    if type(expression[i]) == int:
        if minus_check:
            answer -= expression[i]
        else:
            answer += expression[i]
    elif expression[i] == '-':
        minus_check = True
print(answer)
