import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(f'{x}\n')


def main():
    N = int(input())
    stack = []
    for _ in range(N):
        cmd = input().rstrip()
        if cmd[:4] == 'push':
            n = int(cmd.split()[1])
            stack.append(n)
        elif cmd == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif cmd == 'size':
            print(len(stack))
        elif cmd == 'empty':
            print(int(not bool(stack)))
        elif cmd == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)


if __name__ == '__main__':
    main()
