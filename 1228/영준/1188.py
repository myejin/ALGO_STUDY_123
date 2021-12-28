"""
Title : 음식 평론가
Link : https://www.acmicpc.net/problem/1188
"""

from math import gcd
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
print(M - gcd(N, M))

'''
각자 N / M 개 소시지 가져감
>> 이어붙인 N개의 소시지 생각
>> 이어붙이 소시지를 M등분할 때, 원래 구분된 개수 : gcd(N, M)
'''