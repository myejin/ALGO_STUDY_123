import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()  # 입력받은 수열을 정렬

result = 0

idx = 0

while idx < N:
    # 음수인 경우
    if numbers[idx] < 0:
        # 곱할 수 있는 0 이하의 수가 있을 경우
        if idx+1 < N and numbers[idx+1] <= 0:
            result += numbers[idx]*numbers[idx+1]
            idx += 2
        else:
            result += numbers[idx]
            idx += 1
    # 0 이나 1 이 음수와 곱해지지 않고 남은 경우
    elif numbers[idx] == 0 or numbers[idx] == 1:
        result += numbers[idx]
        idx += 1
    # 양수인 경우
    else:
        # 양수가 홀수만큼 남은 경우
        if (N-idx) % 2:
            result += numbers[idx]
            idx += 1
        # 양수가 짝수만큼 남은 경우
        else:
            result += numbers[idx]*numbers[idx+1]
            idx += 2

print(result)