import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    nums = sorted(map(int, input().split()))
    arr = [[]]
    for num in nums:
        flag = False
        for i in range(len(arr)):
            if len(arr[i]) <= num:
                arr[i].append(num)
                flag = True
                break
        if not flag:
            arr.append([num])
    print(len(arr))


if __name__ == '__main__':
    main()
