import sys


def power(p: int, n: int) -> int:
    if n == 1:
        return p % 1000000007
    val = power(p, n // 2)
    if n % 2 == 0:
        return val * val % 1000000007
    else:
        return val * val * p % 1000000007


def main():
    K, P, N = map(int, sys.stdin.readline().split())
    P = power(P, 10)
    answer = K * power(P, N) % 1000000007
    sys.stdout.write(f'{answer}')


if __name__ == '__main__':
    main()
