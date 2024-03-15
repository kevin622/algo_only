import sys


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    prefix_sum = [0] + list(map(int, input().split()))

    for i in range(N):
        prefix_sum[i + 1] += prefix_sum[i]
        prefix_sum[i + 1] %= M

    cnt = [0] * M
    for i in range(1, N + 1):
        cnt[prefix_sum[i]] += 1

    answer = cnt[0]
    for i in range(M):
        if cnt[i] >= 2:
            answer += cnt[i] * (cnt[i] - 1) // 2
    print(answer)


if __name__ == "__main__":
    main()
