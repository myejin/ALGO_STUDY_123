"""
Title : 트리 순회
Link : https://www.acmicpc.net/problem/1991
"""

import sys
input = sys.stdin.readline


def preorder(tree: list, now: str) -> str:
    ans = now
    now = ord(now) - 65
    if tree[now][1] != '.':
        ans += preorder(tree, tree[now][1])
    if tree[now][2] != '.':
        ans += preorder(tree, tree[now][2])
    return ans


def inorder(tree: list, now: str) -> str:
    ans = ''
    now = ord(now) - 65
    if tree[now][1] != '.':
        ans += inorder(tree, tree[now][1])
    ans += chr(now + 65)
    if tree[now][2] != '.':
        ans += inorder(tree, tree[now][2])
    return ans


def postorder(tree: list, now: str) -> str:
    ans = ''
    now = ord(now) - 65
    if tree[now][1] != '.':
        ans += postorder(tree, tree[now][1])
    if tree[now][2] != '.':
        ans += postorder(tree, tree[now][2])
    ans += chr(now + 65)
    return ans


# A의 아스키 65
n = int(input())
tree = [[] for _ in range(26)]
for _ in range(n):
    tmp = list(input().strip().split())
    m = ord(tmp[0]) - 65
    tree[m] = tmp


print(preorder(tree, 'A'))
print(inorder(tree, 'A'))
print(postorder(tree, 'A'))
