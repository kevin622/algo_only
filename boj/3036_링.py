import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))


def get_gcd(n: int, m: int):
    if m == 0:
        return n
    return get_gcd(m, n % m)


num = arr[0]
for i in range(1, N):
    gcd = get_gcd(num, arr[i])
    print(f'{num // gcd}/{arr[i] // gcd}')
