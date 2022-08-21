import sys
from collections import deque

sys.setrecursionlimit(200000)
N, K = map(int, sys.stdin.readline().split())
dp = [-1] * (2 * K + 1)
indices = [-1] * (2 * K + 1)


def main():
    if K <= N:
        print(N - K)
        print(*range(N, K - 1, -1))
        return

    queue = deque([(0, N)])
    while queue:
        depth, n = queue.popleft()
        dp[n] = depth
        if n == K:
            break
        if 0 <= 2 * n < len(dp) and dp[2 * n] == -1 and indices[2 * n] == -1:
            queue.append((depth + 1, 2 * n))
            indices[2 * n] = n
        if 0 <= (n - 1) < len(dp) and dp[(n - 1)] == -1 and indices[(n - 1)] == -1:
            queue.append((depth + 1, n - 1))
            indices[(n - 1)] = n
        if 0 <= (n + 1) < len(dp) and dp[n + 1] == -1 and indices[n + 1] == -1:
            queue.append((depth + 1, n + 1))
            indices[n + 1] = n
    print(dp[K])
    arr = [K]
    num_before = K
    while num_before != N:
        num_before = indices[num_before]
        arr.append(num_before)
    print(*arr[::-1])


if __name__ == '__main__':
    main()
