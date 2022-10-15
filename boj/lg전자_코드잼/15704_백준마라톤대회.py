import sys
from heapq import heappop, heappush


def is_over_cost(p: int, connection: list[list[int]], N: int, K: int):
    # dijkstra
    dis = [-1] * (N + 1)
    heap = []
    heappush(heap, (0, 1))
    while heap:
        curr_cost, v = heappop(heap)
        if dis[v] == -1 or curr_cost < dis[v]:
            dis[v] = curr_cost
            if v == N:
                break
            for next_v, c, t in connection[v]:
                if p <= t:
                    next_cost = 0
                else:
                    next_cost = c * (p - t) * (p - t)
                new_cost = curr_cost + next_cost
                if dis[next_v] == -1 or new_cost < dis[next_v]:
                    heappush(heap, (new_cost, next_v))
    return dis[N] > K or dis[N] == -1


def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    connection = [[] for _ in range(N + 1)]
    for _ in range(M):
        v1, v2, C, T = map(int, input().split())
        connection[v1].append([v2, C, T])
        connection[v2].append([v1, C, T])

    # 이분탐색
    left = 1
    right = 100000
    while left <= right:
        mid = (left + right) // 2
        if is_over_cost(mid, connection, N, K):
            right = mid - 1
        else:  # cost <= K
            left = mid + 1
    print(right)


if __name__ == '__main__':
    main()
