import sys
from heapq import heappop, heappush


def main():
    N, M = map(int, sys.stdin.readline().split())
    orders = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    connections = {i: [] for i in range(1, N + 1)}
    edge_cnt = [0] * (N + 1)
    for a, b in orders:
        connections[a].append(b)
        edge_cnt[b] += 1
    heap = []
    for i in range(1, N + 1):
        if edge_cnt[i] == 0:
            heappush(heap, i)
    answer = []
    while len(answer) != N:
        val = heappop(heap)
        answer.append(val)
        for n_val in connections[val]:
            edge_cnt[n_val] -= 1
            if edge_cnt[n_val] == 0:
                heappush(heap, n_val)
    print(*answer)


if __name__ == "__main__":
    main()
