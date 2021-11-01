"""
Title : 자료구조는 정말 최고야
Link : https://www.acmicpc.net/problem/23253
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M = MIIS()
dummies = []
books_top_idx = [-1] * (N + 1)
for i in range(M):
    _ = input()
    dummies.append(list(MIIS()))
    books_top_idx[dummies[-1][-1]] = i

book_now = 1
while True:
    # 마지막 책은 확인할 없음
    if book_now == N:
        break
    # 다음 책을 꺼내지 못할 때
    elif books_top_idx[book_now] == -1:
        break
    # 다음 책이 있는 더미의 인덱스
    dummy_idx = books_top_idx[book_now]
    # 책 빼기
    dummies[dummy_idx].pop()
    # 더미가 남아 있으면 다음 책 설정
    if dummies[dummy_idx]:
        books_top_idx[dummies[dummy_idx][-1]] = dummy_idx
    book_now += 1

if book_now == N:
    print('Yes')
else:
    print('No')
