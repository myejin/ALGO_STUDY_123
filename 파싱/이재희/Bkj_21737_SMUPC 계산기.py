def SMUP_calc(num):
    global SMUPC, result
    if SMUPC == 'S':
        result -= num
    elif SMUPC == 'M':
        result *= num
    elif SMUPC == 'U':
        if result < 0:
            result = -((-result) // num)
        else:
            result = result // num
    elif SMUPC == 'P':
        result += num
    else:
        result = num


N = int(input())
words = str(input())

SMUPC = ''  # 이전 기호
now_num = ''
result = 0
C_check = False

for word in words:
    # 새로운 기호가 발견되면 이전 기호 연산을 수행
    if word in 'SMUPC':
        # 이전 기호가 'C'라면 연산을 수행하지 않음
        if SMUPC != 'C':
            num = int(now_num)
            SMUP_calc(num)
        if word == 'C':
            C_check = True
            print(result, end=' ')
        SMUPC = word
        now_num = ''
    else:
        now_num += word

if not C_check:
    print('NO OUTPUT')