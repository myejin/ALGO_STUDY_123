import sys
input = sys.stdin.readline
T = int(input())


def binary(num):
    if num < 2:
        return str(num)
    return binary(num // 2) + str(num % 2)


def decimal(num):
    temp = 0
    idx = 0
    for k in range(len(num)-1, -1, -1):
        if int(num[idx]):
            temp += 2**k
        idx += 1
    return temp


for tc in range(1, T+1):
    # 부호 X : 1, 부호 O : 2
    M, N = input().split()
    if M == '1':
        answer = 0
        n_list = N.split('.')
        for i in range(0, 8):
            answer += int(n_list[i])*(256**(7-i))
        print(answer)

    else:
        b_n = binary(int(N))
        b_n = '0'*(64 - len(b_n)) + b_n
        print('.'.join([str(decimal(b_n[i:i+8])) for i in range(0, len(b_n), 8)]))

