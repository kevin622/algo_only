import sys

input = sys.stdin.readline


def main():
    N, C = map(int, input().split())
    arr = sorted(map(int, input().split()))
    sum_weight = [0]
    for i in range(N):
        sum_weight.append(sum_weight[i] + arr[i])


if __name__ == '__main__':
    main()
