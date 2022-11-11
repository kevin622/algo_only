import sys


def find_head(n: int, heads: list[int]) -> int:
    if heads[n] != n:
        heads[n] = find_head(heads[n], heads)
    return heads[n]


def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    arr: list[tuple] = [(i, *map(int, input().split())) for i in range(1, M + 1)]
    arr.reverse()
    answers = [-1]
    for k in range(K):
        if answers[-1] == 0:
            answers.extend([0] * (K - k))
            break
        heads = list(range(N + 1))
        answer = 0
        cnt = 0
        for i in range(len(arr) - 1, -1, -1):
            weight, a, b = arr[i]
            a, b = min(a, b), max(a, b)
            a_head: int = find_head(a, heads)
            b_head: int = find_head(b, heads)
            if a_head == b_head:
                continue
            heads[b_head] = heads[a_head]
            answer += weight
            cnt += 1
            if cnt == (N - 1):
                break
        if cnt != (N - 1):
            answer = 0
        answers.append(answer)
        arr.pop()

    print(" ".join(map(str, answers[1:])))


if __name__ == '__main__':
    main()
