import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def main():
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]
    times.sort()
    answer = 0
    heap = []
    for s, e in times:
        if not heap or heap[0] > s:
            heappush(heap, e)
            answer = max(len(heap), answer)
        else:
            heappop(heap)
            heappush(heap, e)

    print(answer)


if __name__ == '__main__':
    main()
