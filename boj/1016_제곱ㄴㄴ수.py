import sys

n, m = map(int, sys.stdin.readline().split())
check = [1] * (m - n + 1)
for i in range(2, int(m ** 0.5) + 1):
    val = i ** 2
    rest = n % val
    idx = 0 if rest == 0 else -rest + val
    length = (len(check) - idx - 1) // val + 1
    check[idx::val] = [0] * length
print(sum(check))
