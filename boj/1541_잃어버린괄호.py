import sys


def main():
    equation = sys.stdin.readline().rstrip()
    nums = []
    ops = []
    num = ''
    for i in range(len(equation)):
        if equation[i].isdigit():
            num += equation[i]
        else:
            nums.append(int(num))
            num = ''
            ops.append(equation[i])
    nums.append(int(num))

    answer = nums[0]
    flag = False
    for i in range(len(ops)):
        if ops[i] == '-':
            flag = True
            answer -= nums[i + 1]
        else:
            if flag:
                answer -= nums[i + 1]
            else:
                answer += nums[i + 1]

    sys.stdout.write(str(answer))


if __name__ == "__main__":
    main()
