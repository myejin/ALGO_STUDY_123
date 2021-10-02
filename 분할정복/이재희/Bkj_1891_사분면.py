# 숫자의 행이나 열의 좌표를 탐색
def find_loca(num, check):
    num = str(num)
    start = 0
    end = 2**(d)-1
    # 높은 자리부터 탐색
    for i in range(d):
        # check에 속하는지 아닌지에 따라 판별
        if num[i] in check:
            end = (start+end) // 2
        else:
            start = (start+end) // 2 + 1
    return start

# 좌표를 통해 숫자를 탐색
def find_num(i, j):
    result = ''
    mid_i = 2**(d) // 2
    mid_j = 2**(d) // 2
    # 숫자의 자릿수만큼 탐색
    for k in range(1, d+1):
        # i, j의 크기에 따라 4번 분기
        if i < (mid_i):
            if j < (mid_j):
                result += '2'
                mid_j -= 2**(d-k) // 2
            else:
                result += '1'
                mid_j += 2**(d-k) // 2
            mid_i -= 2**(d-k) // 2
        else:
            if j < (mid_j):
                result += '3'
                mid_j -= 2**(d-k) // 2
            else:
                result += '4'
                mid_j += 2**(d-k) // 2
            mid_i += 2**(d-k) // 2
    return result


d, number = map(int, input().split())
x, y = map(int, input().split())

i = find_loca(number, ['1', '2'])
j = find_loca(number, ['2', '3'])

# 주어진 x, y만큼 좌표를 이동
i, j = i-y, j+x

# 이동된 좌표가 사분면을 벗어나는지 확인
if 0 <= i < 2**d and 0 <= j < 2**d:
    print(find_num(i, j))
else:
    print(-1)