import sys


def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        input()
        A = sorted(map(int, input().split()))
        B = sorted(map(int, input().split()))
        answer = 0
        a = 0
        b = 0
        while a < len(A):
            if (b + 1) < len(B):
                while abs(A[a] - B[b]) > abs(A[a] - B[b + 1]):
                    b += 1
                    if (b + 1) == len(B):
                        break
            answer += B[b]
            a += 1
        print(answer)


if __name__ == '__main__':
    main()
