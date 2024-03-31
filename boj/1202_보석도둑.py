import sys
import heapq


def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    jewels = sorted([list(map(int, input().split())) for _ in range(N)],
                    key=lambda x: x[0])  # weight, value
    bags = sorted([int(input()) for _ in range(K)])
    heap = []
    pointer_jewel = 0
    pointer_bag = 0
    answer = 0
    while pointer_jewel <= N and pointer_bag < K:
        if pointer_jewel < N and jewels[pointer_jewel][0] <= bags[pointer_bag]:
            val = jewels[pointer_jewel]
            heapq.heappush(heap, (-val[1], val[0]))
            pointer_jewel += 1
        else:
            if heap:
                answer += -heapq.heappop(heap)[0]
            pointer_bag += 1
    print(answer)


if __name__ == "__main__":
    main()
