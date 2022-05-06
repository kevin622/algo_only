import sys
import heapq

input = sys.stdin.readline


def print_(x):
    sys.stdout.write(f'{x}\n')


def main():
    N = int(input())
    M = int(input())
    connections = {i: dict() for i in range(1, N + 1)}
    for _ in range(M):
        v1, v2, cost = map(int, input().split())
        connections[v1][v2] = min(connections[v1].get(v2, 100000), cost)
    A, B = map(int, input().split())

    # dijkstra
    INF = int(1e10)
    dis = [INF] * (N + 1)
    heap = [(0, A)]
    while True:
        cost, v = heapq.heappop(heap)
        if v == B:
            print_(cost)
            break
        for next_v in connections[v]:
            next_cost = cost + connections[v][next_v]
            if next_cost < dis[next_v]:
                dis[next_v] = next_cost
                heapq.heappush(heap, (next_cost, next_v))


if __name__ == '__main__':
    main()
