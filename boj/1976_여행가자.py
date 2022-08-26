import sys


def get_set(v: int, sets: list) -> int:
    if sets[sets[v]] != sets[v]:
        sets[v] = get_set(sets[v], sets)
    return sets[v]


def union(v1: int, v2: int, sets: list) -> None:
    v1, v2 = min(v1, v2), max(v1, v2)
    v1_set = get_set(v1, sets)
    v2_set = get_set(v2, sets)
    if v1_set != v2_set:
        sets[v2_set] = v1_set


def main():
    input = sys.stdin.readline
    N = int(input())
    sys.setrecursionlimit(N + 5)
    M = int(input())
    sets = list(range(N + 1))
    for i in range(1, N + 1):
        arr = list(map(int, input().split()))
        for j in range(1, N + 1):
            if arr[j - 1]:
                union(i, j, sets)

    cities = list(map(int, input().split()))
    first_set = get_set(cities[0], sets)
    answer = 'YES'
    for i in range(1, M):
        if get_set(cities[i], sets) != first_set:
            answer = 'NO'
    print(answer)


if __name__ == '__main__':
    main()
