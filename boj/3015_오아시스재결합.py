import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    stack: list[list[int]] = []
    answer = 0
    for _ in range(N):
        num = int(input())
        while stack and stack[-1][0] < num:
            answer += stack.pop()[1]
        if stack:
            if stack[-1][0] == num:
                answer += stack[-1][1]
                if len(stack) >= 2:
                    answer += 1
                stack[-1][1] += 1
            else:
                answer += 1
                stack.append([num, 1])
        else:
            stack.append([num, 1])
        # print(num, stack, answer)
    print(answer)


if __name__ == "__main__":
    main()
