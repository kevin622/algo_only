import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))
    answer = [0] * N
    stack = []
    for i in range(N):
        num = arr[i]
        while stack and arr[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(i)
    for j in stack:
        answer[j] = -1
    print(*answer)


if __name__ == "__main__":
    main()
