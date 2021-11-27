# S3 23252 블록
# https://www.acmicpc.net/problem/23252
# 많은 조건 분기
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    lst = list(map(int, input().split()))
    if not lst[0] and not lst[1] and not lst[2]:
        print('No')
        continue
    if lst[0] >= lst[2]:  # 1개는 무조건 3개보다 크거나 같아야함.
        if not lst[1] % 2 and not (lst[0]-lst[2]) % 2:  # 2개도 짝수이면서 1개 - 3개도 짝수.
            print('Yes')
            continue
        if lst[1] % 2 and lst[0] > lst[2] and not (lst[0]-lst[2]) % 2:  # 2개가 홀수이지만, 1개가 짝수개로 남아있음.
            print('Yes')
            continue
        if lst[1] % 2 and lst[2] and not (lst[0]-lst[2]) % 2:  # 2개가 홀수개이지만 , 1개와 3개가 있어 (1 + 2 + 3)을 만들 수 있음. (3개가 있고, 1개 - 3개도 짝수)
            print('Yes')
            continue
    print('No')


    # if not lst[0] and not lst[1] and not lst[2]:  # 다 0이면 No
    #     print('No')
    #     continue
    # # 3개 타일은 1이 무조건 1개 필요하다. ( 1개 타일 개수 > 3개 타일 개수)
    # tmp[0] -= tmp[2]
    # if tmp[0] < 0:
    #     print('No')
    #     continue
    # # 1개 타일은 3개 타일과 함께 거나 2의 배수여야함.
    # if tmp[0] % 2:
    #     print('No')
    #     continue
    # # 2개 타일은 2의 배수거나 2개타일이 홀수 일 경우 1이 짝수개 이거나 2 + 1 + 3이여야함.
    # if tmp[1] % 2:
    #     if not tmp[0] % 2:  # 3개 타일 없고 1개 타일이 짝수개일경우는 yes.
    #         print('Yes')
    #         continue
    #     if lst[0] == 0 or lst[2] == 0:  # 위에서 조건으로 다 제외했기 때문에 2 + 1 + 3은 그냥 1개 타일과 3개타일이 존재하는지만 확인하면 된다.
    #         print('No')
    #         continue
    # print('Yes')

# 최소 필요 개수들 총 5가지임.
# (1 + 1) / (1 + 3) / (1 + 1 + 2) / (1 + 2 + 3) / (2 + 2)
