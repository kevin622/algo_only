import sys


def get_sign(n: int):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def main():
    input = sys.stdin.readline
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    inner_product: int = (x2 - x1) * (y3 - y2) - (x3 - x2) * (y2 - y1)
    print(get_sign(inner_product))


if __name__ == '__main__':
    main()
