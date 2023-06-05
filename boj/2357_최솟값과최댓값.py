import sys
import math


class SegmentTree:
    def __init__(self, arr: list, is_min: bool):
        self.arr = arr
        self.is_min = is_min
        self.arr_len = len(arr)
        self.tree_len = 2 ** (int(math.log(len(arr), 2)) + 2)
        self.tree = [0] * self.tree_len
        self._create_tree(start=0, end=len(arr) - 1)
        self.MAX_VAL = max(arr)
        self.MIN_VAL = min(arr)

    def _create_tree(self, start, end, idx: int = 1):
        if start == end:
            self.tree[idx] = self.arr[start]
            return
        self._create_tree(start, (start + end) // 2, idx * 2)
        self._create_tree((start + end) // 2 + 1, end, idx * 2 + 1)
        if self.is_min:
            self.tree[idx] = min(self.tree[idx * 2], self.tree[idx * 2 + 1])
        else:
            self.tree[idx] = max(self.tree[idx * 2], self.tree[idx * 2 + 1])

    def get_value(self, left, right):
        return self._get_value(
            start=0,
            end=self.arr_len - 1,
            left=left,
            right=right
        )

    def _get_value(self, start, end, left, right, idx=1):
        """
        start, end: value for tree
        left, right: value for arr
        idx: tree index
        """
        if end < left or right < start:
            return self.MAX_VAL if self.is_min else self.MIN_VAL
        if left <= start and end <= right:
            return self.tree[idx]
        if self.is_min:
            return min(
                self._get_value(start, (start + end) // 2, left, right, idx * 2),
                self._get_value((start + end) // 2 + 1, end, left, right, idx * 2 + 1)
            )
        else:  # getting max value
            return max(
                self._get_value(start, (start + end) // 2, left, right, idx * 2),
                self._get_value((start + end) // 2 + 1, end, left, right, idx * 2 + 1)
            )


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    min_segment_tree = SegmentTree(arr=arr, is_min=True)
    max_segment_tree = SegmentTree(arr=arr, is_min=False)
    for _ in range(M):
        a, b = map(int, input().split())
        print(min_segment_tree.get_value(a - 1, b - 1), max_segment_tree.get_value(a - 1, b - 1))


if __name__ == '__main__':
    main()
