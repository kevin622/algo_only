from heapq import heappop, heappush
import sys

input = sys.stdin.readline


def main():
    N = int(input())
    heap = []
    for _ in range(N):
        x = int(input())
        if x > 0:
            heappush(heap, -x)
        else:
            answer = 0
            if heap:
                answer = -heappop(heap)
            print(answer)


if __name__ == '__main__':
    main()
