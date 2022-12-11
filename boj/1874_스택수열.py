import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    arr = [0] * (N + 1)
    answer = []
    stack = []
    num = 1
    for _ in range(N):
        n = int(input())
        if arr[n] == 1:
            while stack[-1] != n:
                arr[stack.pop()] = -1
                answer.append('-')
            arr[stack.pop()] = -1
            answer.append('-')
        elif arr[n] == 0:
            while num != n:
                stack.append(num)
                arr[num] = 1
                num += 1
                answer.append('+')
            stack.append(num)
            arr[num] = 1
            num += 1
            answer.append('+')
            arr[stack.pop()] = -1
            answer.append('-')
        else:
            print('NO')
            return
    print('\n'.join(answer))


if __name__ == '__main__':
    main()
