import sys


def main():
    _ = sys.stdin.readline()
    nums = list(map(int, sys.stdin.readline().split()))
    vec = [0]
    for num in nums:
        if vec[-1] < num:
            vec.append(num)
        else:
            left = 0
            right = len(vec) - 1
            while left <= right:
                mid = (left + right) // 2
                if vec[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            vec[left] = num
    sys.stdout.write(str(len(vec) - 1))


if __name__ == '__main__':
    main()
