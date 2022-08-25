import sys

input = sys.stdin.readline
sys.setrecursionlimit(100005)

n = int(input())
inorder_arr = list(map(int, input().split()))
inorder_idx = {inorder_arr[i]: i for i in range(n)}
postorder_arr = list(map(int, input().split()))

answer = []


def preorder(in_start: int = 0, in_end: int = n - 1, post_start: int = 0, post_end: int = n - 1):
    if in_start > in_end:
        return
    root = postorder_arr[post_end]
    answer.append(root)
    if in_start == in_end:
        return
    in_root_idx: int = inorder_idx[root]
    left_len = in_root_idx - in_start

    preorder(in_start, in_root_idx - 1, post_start, post_start + left_len - 1)
    preorder(in_root_idx + 1, in_end, post_start + left_len, post_end - 1)


def main():
    preorder()
    print(*answer)


if __name__ == '__main__':
    main()
