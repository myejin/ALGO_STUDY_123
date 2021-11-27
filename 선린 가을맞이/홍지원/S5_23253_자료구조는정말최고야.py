# S5 25253 자료구조는 정말 최고야
# https://www.acmicpc.net/problem/23253
# 구현, 자료 구조, 애드 혹, 스택
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dummy = []
book = []
flag = True
for _ in range(M):
    dummy.append(int(input()))
    temp = list(map(int, input().split()))
    temp_sort = sorted(temp, reverse=True)             # 내림차순 한 다음 정렬 전과 다르면 뽑을 수 없는 것이므로 False 해줌
    if temp != temp_sort:
        flag = False
        break
if flag:
    print('Yes')
else:
    print('No')


# 시간 초과 뜸... 정렬로 아주 쉽게 풀렸다..
# N, M = map(int, input().split())
# dummy = []
# book = []
# for _ in range(M):
#     dummy.append(int(input()))
#     book.append(list(map(int, input().split())))
#
# N_idx = 0
# order = [0] * M  # 각 더미에서 제일 최근에 꺼내온 책 번호
# for i in range(M):  # 맨 위에 있는 책 번호 꺼내기
#     if N in book[i]:  # 제일 마지막 번호 교과서가 있는 더미 구하기
#         N_idx = i
#     order[i] = book[i].pop()
#
# idx = 1
# flag = True
# while idx < N:  # 제일 마지막 번호가 pop 됐거나 그 더미가 다 없어지면 while 문을 빠져나옴.
#     if idx in order:  # 맨 위에 있는 책들 중 순서가 있으면 해당 더미에서 제일 위에 책을 pop 해서 order 에 저장.
#         i = order.index(idx)
#         if book[i]:  # 해당 더미에 pop 할 책이 있으면 pop 하고 없으면 넘어감.
#             order[i] = book[i].pop()
#         idx += 1
#     else:  # 순서의 책이 제일 위에 없음.
#         flag = False
#         break
#
# if flag:
#     print('Yes')
# else:
#     print('No')


# 그냥 제일 위에 있는거에서 순서의 책을 찾고 있으면 그다음 그 위치의 더미에서 제일 위에 책 가지고 오고
# 뽑을 수 없으면 false 임.

# 아마 그냥 받을 때 sort 말고 앞에 값이 뒤에 값보다 큰 지 확인하고 break 해서
# 출력하는게 문제 의도 인듯.
# stack 으로 풀 수 있긴함. 나는 너무 많이 돌고 책 번호 만큼 돌게 끔 만들어 줄 수 있을듯
