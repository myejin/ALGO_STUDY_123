import sys
input = sys.stdin.readline


def preorder(tree: dict, now: str):
    print(now,end='')
    if tree[now][0] != '.':
        preorder(tree, tree[now][0])
    if tree[now][1] != '.':
        preorder(tree, tree[now][1])


def inorder(tree: dict, now: str):
    if tree[now][0] != '.':
        inorder(tree, tree[now][0])
    print(now, end='')
    if tree[now][1] != '.':
        inorder(tree, tree[now][1])


def postorder(tree: dict, now: str):
    if tree[now][0] != '.':
        postorder(tree, tree[now][0])
    if tree[now][1] != '.':
        postorder(tree, tree[now][1])
    print(now, end='')


N = int(input())
tree = {}
for _ in range(N):
    a, b, c = input().split()
    tree[a] = [b, c]

preorder(tree, 'A')
print()
inorder(tree, 'A')
print()
postorder(tree, 'A')