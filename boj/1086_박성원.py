# https://suuntree.tistory.com/124
# https://velog.io/@jini_eun/%EB%B0%B1%EC%A4%80-1086%EB%B2%88-%EB%B0%95%EC%84%B1%EC%9B%90-Java-Python

import sys
import math

'''
- dp[i][j] : i(비트)번 숫자들을 사용했을 때 나머지가 j(정수)인 경우의 수 (j ≤ K)
- dp[0][0] = 1

- dp[i | (1 << l)][next] : i에 속하지 않은 l번째 숫자를 뒤에 붙였을 때 나머지가 next인 경우의 수
    => dp[i | (1 << l)][next] += dp[i][j]
- next  = (새로 만들어진 수) % K
        = ((원래 수) * 10^(len(l번째 수)) + (l번째 수)) % K
        = (((원래 수) % K) * (10^(len(l번째 수)) % K) + ((l번째 수) % K)) % K 
        = (j * (10^(len(arr[l])) % K) + (arr[l] % K)) % K 
        즉 l(<N)과 j(<K) 값만 있으면 구할 수 있다. 
'''


def main():
    input = sys.stdin.readline
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    K = int(input())
    dp = [[0] * K for _ in range(1 << N)]
    dp[0][0] = 1

    next_vals = []
    for n in range(N):
        temp = []
        for k in range(K):
            temp.append((k * (10 ** (len(str(arr[n]))) % K) + (arr[n] % K)) % K)
        next_vals.append(temp)

    for i in range(1 << N):
        for l in range(N):
            if i & (1 << l):
                continue
            for j in range(K):
                # next_val = (j * (10^(len(arr[l])) % K) + (arr[l] % K)) % K
                next_val = next_vals[l][j]
                dp[i | (1 << l)][next_val] += dp[i][j]
    p = dp[(1 << N) - 1][0]
    q = sum(dp[(1 << N) - 1])
    g = math.gcd(p, q)
    print(f"{p // g}/{q // g}")


if __name__ == '__main__':
    main()
