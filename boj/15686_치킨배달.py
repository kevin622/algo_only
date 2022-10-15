import sys
from itertools import combinations

min_dist = int(1e10)


def update_min_dist(indices: list[int], dist: list[list[tuple[int]]]):
    global min_dist
    sum_dist = 0
    for arr in dist:
        for d, i in arr:
            if i in indices:
                sum_dist += d
                break
        if sum_dist > min_dist:
            return
    min_dist = min(min_dist, sum_dist)


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    ones = []
    twos = []
    for i in range(N):
        arr = list(map(int, input().split()))
        for j in range(N):
            if arr[j] == 1:
                ones.append((i, j))
            elif arr[j] == 2:
                twos.append((i, j))

    dist = [[] for _ in range(len(ones))]
    for idx1, (x1, y1) in enumerate(ones):
        for idx2, (x2, y2) in enumerate(twos):
            dist[idx1].append((abs(x1 - x2) + abs(y1 - y2), idx2))
        dist[idx1].sort()

    for i in range(1, M + 1):
        for indices in combinations(range(len(twos)), i):
            update_min_dist(indices, dist)
    print(min_dist)


if __name__ == '__main__':
    main()
