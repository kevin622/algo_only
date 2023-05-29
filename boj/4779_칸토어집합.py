import sys


def get_answer(n: int) -> str:
    if n == 0:
        return '-'
    next_answer = get_answer(n - 1)
    return next_answer + (' ' * len(next_answer)) + next_answer


def main():
    input = sys.stdin.readline
    while True:
        str_n = input()
        if not str_n:
            return
        N = int(str_n)
        answer = get_answer(N)
        print(answer)


if __name__ == "__main__":
    main()
