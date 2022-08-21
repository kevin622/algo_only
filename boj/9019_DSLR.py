import sys
from collections import deque


def main():
    input = sys.stdin.readline
    T = int(input())
    for tc in range(T):
        A, B = map(int, input().split())
        dp = [-1] * 10000
        dp_str = [''] * 10000
        num = A
        dp[num] = 0
        queue = deque([num])
        while queue:
            num = queue.popleft()
            if num == B:
                break
            # D
            D = (num * 2)
            if D > 9999:
                D %= 10000
            if dp[D] == -1:
                queue.append(D)
                dp[D] = num
                dp_str[D] = 'D'
            # S
            S = (num - 1) % 10000
            if dp[S] == -1:
                queue.append(S)
                dp[S] = num
                dp_str[S] = 'S'
            # L
            L = (num % 1000) * 10 + (num // 1000)
            if dp[L] == -1:
                queue.append(L)
                dp[L] = num
                dp_str[L] = 'L'
            # R
            R = (num % 10) * 1000 + (num // 10)
            if dp[R] == -1:
                queue.append(R)
                dp[R] = num
                dp_str[R] = 'R'
        answer = ''
        while num != A:
            answer = dp_str[num] + answer
            num = dp[num]
        print(answer)


if __name__ == '__main__':
    main()
