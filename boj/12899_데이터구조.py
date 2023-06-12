import sys

segment_tree = [0] * (1 << 22)
sub_val = -1


def add_value_to_tree(n: int, idx: int, left: int, right: int):
    segment_tree[idx] += 1
    if left == right:
        return
    mid = (left + right) // 2
    if left <= n <= mid:
        add_value_to_tree(n, idx * 2, left, mid)
    elif (mid + 1) <= n <= right:
        add_value_to_tree(n, idx * 2 + 1, mid + 1, right)
    return


def sub_value_from_tree(n: int, idx: int, left: int, right: int):
    segment_tree[idx] -= 1
    if left == right:
        global sub_val
        sub_val = left
        return
    mid = (left + right) // 2
    left_val = segment_tree[idx * 2]
    right_val = segment_tree[idx * 2 + 1]
    if left_val >= n:
        sub_value_from_tree(n, idx * 2, left, mid)
    elif (n - left_val) <= right_val:
        sub_value_from_tree(n - left_val, idx * 2 + 1, mid + 1, right)
    return


def main():
    input = sys.stdin.readline
    N = int(input())
    for _ in range(N):
        T, X = map(int, input().split())
        if T == 1:
            # add X
            add_value_to_tree(X, 1, 0, 2000000)
        else:
            sub_value_from_tree(X, 1, 0, 2000000)
            print(sub_val)


if __name__ == "__main__":
    main()
