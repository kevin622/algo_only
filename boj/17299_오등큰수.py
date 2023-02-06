import sys


def main():
	input = sys.stdin.readline
	N = int(input())
	arr = list(map(int, input().split()))
	cnt = [0] * (max(arr) + 1)
	for num in arr:
		cnt[num] += 1 
	ngf = [-1] * N
	stack = []
	for i in range(N):
		while stack and cnt[arr[i]] > cnt[arr[stack[-1]]]:
			ngf[stack.pop()] = arr[i]
		stack.append(i)
	print(*ngf)

	
if __name__ == '__main__':
	main()

