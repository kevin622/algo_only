import sys


def main():
    while True:
        nums = sys.stdin.readline().rstrip()
        if nums == '0':
            return
        nums = list(map(int, nums.split()))
        n = nums[0]
        heights = nums[1:]

        heights.append(0)
        stack = [-1]
        answer = 0
        for i in range(n + 1):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                area = height * width
                answer = max(answer, area)
            stack.append(i)
        print(answer)


if __name__ == '__main__':
    main()
