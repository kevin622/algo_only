import sys

input = sys.stdin.readline


# power
def power(a, b, mod):
    if b == 1:
        return a
    elif b == 0:
        return 1
    return (power(a, b // 2, mod) ** 2) * power(a, b % 2, mod) % mod


def main():
    N, K = map(int, input().split())
    mod = 1000000007

    # factorial
    factorial = list(range(N + 1))
    factorial[0] = 1
    for i in range(3, N + 1):
        factorial[i] = factorial[i] * factorial[i - 1] % mod

    A = factorial[N]
    B = (factorial[N - K] * factorial[K]) % mod
    answer = (A % mod) * (power(B, mod - 2, mod) % mod) % mod
    sys.stdout.write(str(answer))


if __name__ == '__main__':
    main()
