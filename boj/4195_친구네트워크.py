import sys


def get_set(v: str, sets: dict[str, str]) -> str:
    if sets[sets[v]] != sets[v]:
        sets[v] = get_set(sets[v], sets)
    return sets[v]


def union_set(v1: str, v2: str, sets: dict[str, str], name_to_cnt: dict) -> None:
    v1, v2 = min(v1, v2), max(v1, v2)
    v1_set = get_set(v1, sets)
    v2_set = get_set(v2, sets)
    if v1_set != v2_set:
        sets[v2_set] = v1_set
        name_to_cnt[v1_set] += name_to_cnt[v2_set]
    print(name_to_cnt[v1_set])


def main():
    input = sys.stdin.readline
    T = int(input())
    for tc in range(T):
        F = int(input())
        sets = dict()
        name_to_cnt = dict()
        for _ in range(F):
            name1, name2 = input().split()
            if name1 not in sets:
                sets[name1] = name1
                name_to_cnt[name1] = 1
            if name2 not in sets:
                sets[name2] = name2
                name_to_cnt[name2] = 1
            union_set(name1, name2, sets, name_to_cnt)


if __name__ == '__main__':
    main()
