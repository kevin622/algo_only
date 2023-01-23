'''
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

import sys


class Deque:
	def __init__(self, max_len):
		self.max_len = max_len
		self.arr = [0] * (self.max_len + 1)
		self.front = 0
		self.rear = 0


	def is_empty(self):
		if self.rear == self.front:
			return True
		return False


	def is_full(self):
		if (self.rear + 1 % self.max_len) == self.front:
			return True
		return False


	def push_front(self, num):
		if self.is_full():
			return 
		self.arr[self.front] = num
		self.front = (self.front + self.max_len - 1) % self.max_len		

	
	def push_back(self, num):
		if self.is_full():
			return
		self.rear = (self.rear + 1) % self.max_len
		self.arr[self.rear] = num	


	def pop_front(self):
		if self.is_empty():
			return -1
		self.front = (self.front + 1) % self.max_len
		return self.arr[self.front]


	def pop_back(self):
		if self.is_empty():
			return -1
		answer = self.arr[self.rear]
		self.rear = (self.rear - 1 + self.max_len) % self.max_len
		return answer

	
	def get_front(self):
		if self.is_empty():
			return -1
		return self.arr[(self.front + 1) % self.max_len]


	def get_rear(self):
		if self.is_empty():
			return -1
		return self.arr[self.rear]


	def get_size(self):
		if self.is_empty():
			return 0
		return (self.rear - self.front + self.max_len) % self.max_len


def main():
	input = sys.stdin.readline
	N = int(input())
	deque = Deque(N + 1)
	for _ in range(N):
		command = input().rstrip()
		if command[:4] == "push":
			command, i = command.split()
			if command == "push_front":
				deque.push_front(i)
			else:
				deque.push_back(i)
		elif command == "pop_front":
			print(deque.pop_front())	
		elif command == "pop_back":
			print(deque.pop_back())	
		elif command == "size":
			print(deque.get_size())	
		elif command == "empty":
			print(int(deque.is_empty()))
		elif command == "front":
			print(deque.get_front())	
		elif command == "back":
			print(deque.get_rear())

if __name__ == "__main__":
	main()


	
