import sys
from collections import Counter


def main():
    _ = sys.stdin.readline()
    counter = Counter(map(int, sys.stdin.readline().split()))
    _ = sys.stdin.readline()
    answer = list(map(lambda x: counter[int(x)], sys.stdin.readline().split()))
    print(*answer)


if __name__ == '__main__':
    main()