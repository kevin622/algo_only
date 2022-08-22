import sys

input = sys.stdin.readline

N = int(input())
connections = {chr(ord('A') + i): [".", "."] for i in range(N)}
for _ in range(N):
    root, left, right = input().split()
    connections[root][0] = left
    connections[root][1] = right


def preorder(node: str):
    sys.stdout.write(node)
    left = connections[node][0]
    right = connections[node][1]
    if left != '.':
        preorder(left)
    if right != '.':
        preorder(right)


def inorder(node: str):
    left = connections[node][0]
    if left != '.':
        inorder(left)
    sys.stdout.write(node)
    right = connections[node][1]
    if right != '.':
        inorder(right)


def postorder(node: str):
    left = connections[node][0]
    if left != '.':
        postorder(left)
    right = connections[node][1]
    if right != '.':
        postorder(right)
    sys.stdout.write(node)


def main():
    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')


if __name__ == '__main__':
    main()
