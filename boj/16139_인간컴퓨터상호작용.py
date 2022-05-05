import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(f'{x}\n')


def main():
    S = input().rstrip()
    q = int(input())
    alphabets = [chr(i) for i in range(ord('a'), (ord('z') + 1))]
    dp = {s: [0] * (len(S) + 1) for s in alphabets}
    for i in range(1, len(S) + 1):
        letter = S[i - 1]
        dp[letter][i] = 1

    for letter in alphabets:
        for i in range(1, len(S) + 1):
            dp[letter][i] += dp[letter][i - 1]
    for _ in range(q):
        a, L, R = input().split()
        l, r = map(int, [L, R])
        print(dp[a][r + 1] - dp[a][l])


if __name__ == '__main__':
    main()
