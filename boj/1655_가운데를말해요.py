from heapq import heappop, heappush
import sys


def main():
    N = int(sys.stdin.readline())
    min_heap = [int(sys.stdin.readline())]
    max_heap = []
    sys.stdout.write(f'{min_heap[0]}\n')

    for i in range(2, N + 1):
        num = int(sys.stdin.readline())
        if i % 2 == 1:
            heappush(min_heap, num)
        else:
            heappush(max_heap, -num)
        if min_heap[0] < -max_heap[0]:
            max_val = heappop(max_heap)
            min_val = heappop(min_heap)
            heappush(max_heap, -min_val)
            heappush(min_heap, -max_val)
        if i % 2 == 1:
            sys.stdout.write(f'{min_heap[0]}\n')
        else:
            sys.stdout.write(f'{min(min_heap[0], -max_heap[0])}\n')


if __name__ == '__main__':
    main()
