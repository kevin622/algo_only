import sys
from collections import deque


def main():
    input = sys.stdin.readline
    N = int(input())
    queue = deque()
    while True:
        n = int(input())
        if n == -1:
            break
        elif n == 0:
            queue.popleft()
        elif len(queue) < N:
            queue.append(n)
    if queue:
        print(*queue)
    else:
        print('empty')


if __name__ == '__main__':
    main()
