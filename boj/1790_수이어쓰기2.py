'''
1 ~ 9: 0, 1, ..., 8 => i * 1 - 1
10 ~ 99: 9, 11, 13, ..., 187 => i * 2 - 11
100 ~ 999: 189, 192, ..., 2886 => i * 3 - 111
'''
import sys


def main():
    N, k = map(int, sys.stdin.readline().split())

    # 문자열의 길이 구하기
    # N의 자릿수
    order = len(str(N))
    str_len = N * order - int('1' * order) + order
    if str_len < k:
        print(-1)
        return

    # idx: k번째 수의 자릿수
    idx = 1
    while True:
        last_idx = int('9' * idx) * idx - int('1' * idx) + idx - 1
        if last_idx >= k - 1:
            break
        idx += 1

    # first_idx: 현재 자릿수의 첫 index
    def get_int(s: str):
        if s.isdigit():
            return int(s)
        return 0
    first_idx = get_int('9' * (idx - 1)) * (idx - 1) - get_int('1' * (idx - 1)) + (idx - 1)
    k_order = k - first_idx - 1
    num = 10 ** (idx - 1) + k_order // idx
    print(str(num)[k_order % idx])


if __name__ == "__main__":
    main()
