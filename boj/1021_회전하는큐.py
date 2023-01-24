import sys
from collections import deque


def main():
	input = sys.stdin.readline
	N, M = map(int, input().split())
	nums = list(map(int, input().split()))
	queue = deque(range(1, N + 1))
	answer = 0	
	for num in nums:
		one_side = queue.index(num) 
		other_side = N - one_side	
		if one_side < other_side:
			queue.rotate(-one_side)
			answer += one_side
			N -= 1
			queue.popleft()
		else:
			queue.rotate(other_side)
			answer += other_side
			N -= 1
			queue.popleft()	
	print(answer)


if __name__ == '__main__':
	main()
