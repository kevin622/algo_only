def euclidean_algo(n: int, m: int):
    if m == 0:
        return n
    return euclidean_algo(m, n % m)


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(a * b // euclidean_algo(a, b))
