import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(f'{x}\n')


def main():
    N, M = map(int, input().split())
    remainders = [0] * M
    remainders[0] = 1
    num = 0
    for new_num in map(int, input().split()):
        num = (new_num + num) % M
        remainders[num] += 1

    answer = sum(i * (i - 1) for i in remainders) // 2
    print(answer)


if __name__ == '__main__':
    main()
