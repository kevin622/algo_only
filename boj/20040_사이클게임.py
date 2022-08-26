import sys


def get_set(v: int, sets: list[int]):
    if sets[v] != sets[sets[v]]:
        sets[v] = get_set(sets[v], sets)
    return sets[v]


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    sets = list(range(n))
    for i in range(1, m + 1):
        V1, V2 = map(int, input().split())
        v1, v2 = min(V1, V2), max(V1, V2)
        v1_set = get_set(v1, sets)
        v2_set = get_set(v2, sets)
        if v1_set != v2_set:
            sets[v2_set] = v1_set
        else:
            print(i)
    print(0)


if __name__ == '__main__':
    main()
