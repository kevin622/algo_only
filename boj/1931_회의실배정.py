import sys

input = sys.stdin.readline


def main():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: (x[1], x[0]))
    last_end = 0
    answer = 0
    for start, end in arr:
        if start >= last_end:
            answer += 1
            last_end = end
    sys.stdout.write(f'{answer}\n')


if __name__ == '__main__':
    main()
