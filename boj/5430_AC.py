import sys
from collections import deque

input = sys.stdin.readline
print_ = lambda x: sys.stdout.write(f'{x}\n')


def main():
    T = int(input())
    for _ in range(T):
        commands = input().rstrip()
        n = int(input())
        if n > 0:
            arr = deque(input().rstrip()[1:-1].split(','))
        else:
            input()
            arr = deque([])
        error_occurred = False
        is_reversed = False
        for command in commands:
            if command == 'R':
                is_reversed = not is_reversed
            else:
                if len(arr) == 0:
                    error_occurred = True
                    break
                if is_reversed:
                    arr.pop()
                else:
                    arr.popleft()

        if error_occurred:
            print_('error')
        else:
            if is_reversed:
                arr.reverse()
            answer = ",".join(arr)
            print_(f'[{answer}]')


if __name__ == '__main__':
    main()
