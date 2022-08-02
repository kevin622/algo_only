import sys


class Heap:
    def __init__(self):
        self.heap = [0]

    def get_heap(self):
        return self.heap[1:]

    def heap_push(self, num: int):
        self.heap.append(num)
        idx = len(self.heap) - 1
        while idx > 1:
            if self.heap[idx] < self.heap[idx // 2]:
                self.heap[idx], self.heap[idx // 2] = self.heap[idx // 2], self.heap[idx]
                idx //= 2
            else:
                break

    def heap_pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        answer = self.heap[1]
        self.heap[1] = self.heap.pop()
        idx = 1
        while (idx * 2 + 1) < len(self.heap):
            if self.heap[idx * 2] >= self.heap[idx] and self.heap[idx * 2 + 1] >= self.heap[idx]:
                break
            elif self.heap[idx * 2] < self.heap[idx * 2 + 1]:
                self.heap[idx * 2], self.heap[idx] = self.heap[idx], self.heap[idx * 2]
                idx *= 2
            else:
                self.heap[idx * 2 + 1], self.heap[idx] = self.heap[idx], self.heap[idx * 2 + 1]
                idx = idx * 2 + 1
        if (idx * 2) < len(self.heap):
            if self.heap[idx * 2] < self.heap[idx]:
                self.heap[idx * 2], self.heap[idx] = self.heap[idx], self.heap[idx * 2]
        return answer


def main():
    input = sys.stdin.readline
    N = int(input())
    heap = Heap()
    for _ in range(N):
        x = int(input())
        if x == 0:
            if heap.get_heap():
                print(-heap.heap_pop())
            else:
                print(0)
        else:
            heap.heap_push(-x)


if __name__ == '__main__':
    main()
