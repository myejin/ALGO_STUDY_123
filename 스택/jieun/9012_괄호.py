n = int(input())
for _ in range(n):
    gwals = list(input())
    check = 0
    for gwal in gwals:
        if gwal == '(':
            check += 1

        elif gwal == ')':
            check -= 1

        if check < 0 :
            print('NO')
            break

    if check > 0 :
        print('NO')
    elif check == 0 :
        print('YES')

