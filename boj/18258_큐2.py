import sys


class Queue:
    def __init__(self):
        self.arr = []
        self.front = 0

    def __len__(self):
        return len(self.arr) - self.front

    def push(self, num):
        self.arr.append(num)

    def pop(self):
        if len(self) == 0:
            print(-1)
            return
        print(self.arr[self.front])
        self.front += 1

    def print_size(self):
        print(len(self))

    def print_is_empty(self):
        print(1 if len(self) == 0 else 0)

    def print_front(self):
        print(self.arr[self.front] if len(self) != 0 else -1)

    def print_back(self):
        print(self.arr[-1] if len(self) != 0 else -1)


def main():
    input = sys.stdin.readline
    N = int(input())
    queue = Queue()
    for _ in range(N):
        s = input().rstrip()
        if s[:4] == 'push':
            s, num = s.split()
            num = int(num)
            queue.push(num)
        elif s == 'pop':
            queue.pop()
        elif s == 'size':
            queue.print_size()
        elif s == 'empty':
            queue.print_is_empty()
        elif s == 'front':
            queue.print_front()
        elif s == 'back':
            queue.print_back()


if __name__ == '__main__':
    main()
