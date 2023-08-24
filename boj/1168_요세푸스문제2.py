import sys


class SegmentTree:
    def __init__(self, arr: list[int]):
        self.node = [0] * (1 << 18)
        self.arr = arr

    def init(self, curr: int, left: int, right: int):
        if left == right:
            self.node[curr] = self.arr[left]
        else:
            mid = (left + right) // 2
            self.node[curr] = self.init(2 * curr, left, mid) + self.init(2 * curr + 1, mid + 1, right)
        return self.node[curr]

    def delete(self, curr: int, left: int, right: int, rank: int):
        if left == right:
            self.node[curr] -= 1
            return left
        mid = (left + right) // 2
        if rank <= self.node[2 * curr]:
            ret = self.delete(2 * curr, left, mid, rank)
        else:
            ret = self.delete(2 * curr + 1, mid + 1, right, rank - self.node[2 * curr])
        self.node[curr] = self.node[2 * curr] + self.node[2 * curr + 1]
        return ret


def main():
    N, K = map(int, sys.stdin.readline().split())
    arr = [0] * 100000
    arr[:N] = [1] * N
    segment_tree = SegmentTree(arr=arr)
    segment_tree.init(curr=1, left=0, right=N - 1)

    answer = []
    rank = K
    for i in range(N):
        val = segment_tree.delete(curr=1, left=0, right=N - 1, rank=rank) + 1
        answer.append(val)
        if i < (N - 1):
            rank = (rank + K - 2) % (N - i - 1) + 1
    print(f"<{', '.join(map(str, answer))}>")


if __name__ == "__main__":
    main()
