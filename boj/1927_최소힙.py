import sys
from heapq import heappop, heappush


def main():
    N = int(sys.stdin.readline())
    heap = []
    for _ in range(N):
        x = int(sys.stdin.readline())
        if x > 0:
            heappush(heap, x)
        else:
            answer = 0
            if heap:
                answer = heappop(heap)
            sys.stdout.write(f'{answer}\n')


if __name__ == '__main__':
    main()
