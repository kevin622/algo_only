import sys
import math


class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.arr_len = len(arr)
        self.tree_len = 2 ** (int(math.log(self.arr_len, 2)) + 2)
        self.tree = [0] * self.tree_len
        self._create_tree(0, len(arr) - 1)

    def _create_tree(self, start: int, end: int, idx: int = 1):
        if start == end:
            self.tree[idx] = self.arr[start]
            return
        self._create_tree(start, (start + end) // 2, idx * 2)
        self._create_tree((start + end) // 2 + 1, end, idx * 2 + 1)
        self.tree[idx] = self.tree[idx * 2] + self.tree[idx * 2 + 1]

    def get_sub_sum(self, left, right):
        return self._get_sub_sum(0, self.arr_len - 1, left, right)

    def _get_sub_sum(self, start, end, left, right, idx=1):
        '''
        start, end: value for tree
        left, right: value for arr
        idx: tree index
        '''
        if end < left or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[idx]
        return self._get_sub_sum(start, (start + end) // 2, left, right, idx * 2) + self._get_sub_sum(
            (start + end) // 2 + 1, end, left, right, idx * 2 + 1)

    def change_num(self, val, arr_idx):
        self._change_num(val, arr_idx, 0, self.arr_len - 1)
        self.arr[arr_idx] = val

    def _change_num(self, val, arr_idx, start, end, idx=1):
        if start == end:
            if start == arr_idx:
                self.tree[idx] = val
            return
        if start <= arr_idx <= end:
            self.tree[idx] -= self.arr[arr_idx]
            self.tree[idx] += val
            self._change_num(val, arr_idx, start, (start + end) // 2, idx * 2)
            self._change_num(val, arr_idx, (start + end) // 2 + 1, end, idx * 2 + 1)
        return


def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    segment_tree = SegmentTree(arr)
    for _ in range(M + K):
        a, b, c = map(int, input().split())
        if a == 1:
            segment_tree.change_num(c, b - 1)
        else:
            print(segment_tree.get_sub_sum(b - 1, c - 1))


if __name__ == "__main__":
    main()
