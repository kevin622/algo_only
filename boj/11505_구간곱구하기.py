import sys
import math

'''
5 2 2
1
2
3
4
5
1 3 0
2 2 5
1 5 0
2 3 5
'''


class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [1] * (2 ** (int(math.log(len(arr), 2)) + 2))
        self._create_tree(start=0, end=(len(arr) - 1))

    def _create_tree(self, start: int, end: int, idx: int = 1):
        if start == end:
            self.tree[idx] = self.arr[start]
            return
        self._create_tree(start, (start + end) // 2, idx * 2)
        self._create_tree((start + end) // 2 + 1, end, idx * 2 + 1)
        self.tree[idx] = self.tree[idx * 2] * self.tree[idx * 2 + 1] % 1000000007

    def get_sub_mul(self, left: int, right: int):
        return self._get_sub_mul(0, len(self.arr) - 1, left, right) % 1000000007

    def _get_sub_mul(self, start: int, end: int, left: int, right: int, idx: int = 1):
        if right < start or end < left:
            return 1
        if left <= start and end <= right:
            return self.tree[idx]
        return self._get_sub_mul(start, (start + end) // 2, left, right, idx * 2) * self._get_sub_mul(
            (start + end) // 2 + 1, end, left, right, idx * 2 + 1) % 1000000007

    def change_num(self, val, arr_idx):
        self._change_num(val, arr_idx, 0, len(self.arr) - 1)
        self.arr[arr_idx] = val % 1000000007

    def _change_num(self, val, arr_idx, start, end, tree_idx=1):
        if start == end:
            if start == arr_idx:
                self.tree[tree_idx] = val
        elif start <= arr_idx <= end:
            self.tree[tree_idx] = (self._change_num(val, arr_idx, start, (start + end) // 2,
                                                    tree_idx * 2) % 1000000007) * \
                                  (self._change_num(val, arr_idx, (start + end) // 2 + 1, end,
                                                    tree_idx * 2 + 1) % 1000000007)
        return self.tree[tree_idx]


def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    segment_tree = SegmentTree(arr)

    ops = [list(map(int, input().split())) for _ in range(M + K)]
    for a, b, c in ops:
        if a == 1:
            segment_tree.change_num(c, b - 1)
        else:
            print(segment_tree.get_sub_mul(b - 1, c - 1))


if __name__ == "__main__":
    main()
