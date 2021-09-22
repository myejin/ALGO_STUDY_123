inp = input()
if 'x' not in inp:
    a, b = '', inp
else:
    a, b = inp.split('x')

answer = ''

if a:
    if a == '-2':
        answer += '-'
    elif a != '2':
        answer += str(int(a) // 2)
    answer += 'xx'

if b and b != '0':
    if b == '-1':
        answer += '-'
    elif b == '1':
        pass
    elif b == '+1':
        answer += '+'
    else:
        answer += b  
    answer += 'x'

if a or b != '0':
    answer += '+W'
else:
    answer += 'W'

print(answer)
