def n_to_bin(n, size=64):
    if not n:
        return '0' * size
    ret = ['0'] * size
    i = 0
    while n > 0:
        n, m = divmod(n, 2)
        ret[i] = str(m)
        i += 1
    ret.reverse()
    return ''.join(ret)


def bin_to_n(b):
    ret = 0
    for idx, x in enumerate(b):
        if x == '0':
            continue
        ret += 2 ** (len(b) - idx - 1)
    return ret


T = int(input())
for _ in range(T):
    M, N = input().split()
    if M == '1':
        # IPv8 -> 정수
        ipv8 = list(map(int, N.split('.')))
        bin_addr = ''
        for i in ipv8:
            bin_addr += n_to_bin(i, 8)
        print(bin_to_n(bin_addr))
    else:
        # 정수 -> IPv8
        bin_addr = n_to_bin(int(N))
        i = 0
        while True:
            print(bin_to_n(bin_addr[i:i + 8]), end='')
            i += 8
            if i >= len(bin_addr):
                break
            print(end='.')
        print()
