import sys

sys.setrecursionlimit(10005)
preorder_arr = []
lines = sys.stdin.readlines()
for line in lines:
    preorder_arr.append(int(line.rstrip()))

N = len(preorder_arr)
postorder_arr = [0] * N


def fill_postorder_arr(pre_start, pre_end, post_start, post_end):
    if pre_start > pre_end:
        return
    root = preorder_arr[pre_start]
    postorder_arr[post_end] = root
    if pre_start == pre_end:
        return

    # 이분탐색
    l = pre_start + 1
    r = pre_end
    while l <= r:
        mid = (l + r) // 2
        if preorder_arr[mid] < root:
            l = mid + 1
        else:
            r = mid - 1

    left_idx = r
    left_size = left_idx - pre_start
    if left_idx != -1:
        fill_postorder_arr(pre_start + 1, pre_start + left_size, post_start, post_start + left_size - 1)
    if left_idx != pre_end:
        fill_postorder_arr(pre_start + left_size + 1, pre_end, post_start + left_size, post_end - 1)


def main():
    fill_postorder_arr(0, N - 1, 0, N - 1)
    print('\n'.join(map(str, postorder_arr)))


if __name__ == '__main__':
    main()
