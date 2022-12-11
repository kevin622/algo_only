import sys


def main():
    input = sys.stdin.readline
    while True:
        s = input().rstrip()
        if len(s) == 1:
            break
        stack = []
        flag = False
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if not stack or stack[-1] != '(':
                    print('no')
                    flag = True
                    break
                stack.pop()
            elif c == '[':
                stack.append(c)
            elif c == ']':
                if not stack or stack[-1] != '[':
                    print('no')
                    flag = True
                    break
                stack.pop()
        if not flag:
            if stack or stack:
                print('no')
            else:
                print('yes')
    return


if __name__ == '__main__':
    main()
