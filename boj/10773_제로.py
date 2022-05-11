import sys

input = sys.stdin.readline


def main():
    K = int(input())
    stack = []
    for _ in range(K):
        n = int(input())
        if n == 0:
            stack.pop()
        else:
            stack.append(n)
    sys.stdout.write(str(sum(stack)))


if __name__ == '__main__':
    main()
