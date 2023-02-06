import sys


def main():
	input = sys.stdin.readline
	N = int(input())
	stack = []
	arr =  [0] + [int(input()) for _ in range(N)] + [0]
	stack = [0]
	answer = 0
	for i in range(1, N + 2):
		while stack and arr[i] < arr[stack[-1]]:
			idx = stack.pop()
			answer = max(answer, arr[idx] * (i - 1 - stack[-1]))
		stack.append(i)
	print(answer)


if __name__ == '__main__':
	main()
