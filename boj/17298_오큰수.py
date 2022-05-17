import sys

input = sys.stdin.readline


def main():
    N = int(input())
    arr = list(map(int, input().split()))
    answer = [0] * N
    stack = []
    for i in range(N - 1, -1, -1):
        while stack and arr[i] >= stack[-1]:
            stack.pop()
        if not stack:
            answer[i] = -1
        elif stack[-1] > arr[i]:
            answer[i] = stack[-1]
        stack.append(arr[i])
    print(*answer)


if __name__ == '__main__':
    main()
