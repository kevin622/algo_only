import sys


def get_set(v: int, sets: list):
    if sets[v] != sets[sets[v]]:
        sets[v] = get_set(sets[v], sets)
    return sets[v]


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    sys.setrecursionlimit(n + 5)
    sets = list(range(n + 1))
    for _ in range(m):
        op, v1, v2 = map(int, input().split())
        v1, v2 = sorted([v1, v2])
        v1_set = get_set(v1, sets)
        v2_set = get_set(v2, sets)
        if op == 0:
            sets[v2_set] = v1_set
        elif op == 1:
            print('YES' if v1_set == v2_set else 'NO')


if __name__ == '__main__':
    main()
