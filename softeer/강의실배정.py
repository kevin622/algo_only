import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def main():
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]
    heap = []
    for s, e in times:
        heappush(heap, (e, s))
    answer = 0
    last_end = -1
    while heap:
        e, s = heappop(heap)
        if s >= last_end:
            answer += 1
            last_end = e
    sys.stdout.write(f'{answer}\n')


if __name__ == '__main__':
    main()
