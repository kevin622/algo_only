# 아직 푸는 중
N, K = map(int, input().split())
mod = 1000007

# factorial
factorial = list(range(N + 1))
for i in range(3, N + 1):
    factorial[i] = factorial[i] * factorial[i - 1] % mod


# power
def power(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 1
    return (power(a, b // 2) ** 2) * power(a, b % 2) % mod


answer = factorial[N] * power(factorial[K] * factorial[N - K], mod - 2) % mod
print(answer)
