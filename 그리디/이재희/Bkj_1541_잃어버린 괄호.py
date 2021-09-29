inp = str(input())
inp = inp[::-1]  # 역으로 탐색하기 위해 식 반전

num = ''  # 숫자 입력
num_cnt = 0  # '+'에 의한 누적
result = 0

for i in inp:
    if i in ['+', '-']:
        num_cnt += int(num)
        num = ''
        # '-'인 경우 누적된 값을 결과에서 빼줌
        if i == '-':
            result -= num_cnt
            num_cnt = 0
    else:
        num = i + num

# 남아있는 숫자 합산
result += num_cnt + int(num)

print(result)