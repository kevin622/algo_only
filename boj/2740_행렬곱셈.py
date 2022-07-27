import sys

input = sys.stdin.readline


def transpose(mat: list) -> list:
    return list(zip(*mat))


def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    M, K = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(M)]

    answer = []
    for a_row in A:
        row = []
        for b_row in transpose(B):
            val = 0
            for i in range(M):
                val += a_row[i] * b_row[i]
            row.append(val)
        answer.append(row)

    for r in answer:
        print(*r)


if __name__ == '__main__':
    main()
