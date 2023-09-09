# https://devbull.xyz/python-kmp-algorijeumeuro-munjayeol-cajgi/
import sys


def compute_lps(pattern: str, lps: list[int]):
    length = 0
    idx = 1
    while idx < len(lps):
        if pattern[idx] == pattern[length]:
            length += 1
            lps[idx] = length
            idx += 1
            continue
        if length != 0:
            length = lps[length - 1]
            continue
        lps[idx] = 0
        idx += 1


def kmp_search(target: str, pattern: str):
    found_cnt = 0
    found_indices = []
    lps = [0] * len(pattern)
    compute_lps(pattern, lps)

    target_idx = 0
    pattern_idx = 0
    while target_idx < len(target):
        if pattern[pattern_idx] == target[target_idx]:
            pattern_idx += 1
            target_idx += 1
        else:
            if pattern_idx != 0:
                pattern_idx = lps[pattern_idx - 1]
            else:
                target_idx += 1
        if pattern_idx == len(pattern):
            found_indices.append(target_idx - pattern_idx + 1)
            found_cnt += 1
            pattern_idx = lps[pattern_idx - 1]
    print(found_cnt)
    print(' '.join(map(str, found_indices)))


def main():
    T = sys.stdin.readline().rstrip()
    P = sys.stdin.readline().rstrip()
    kmp_search(T, P)


if __name__ == "__main__":
    main()
