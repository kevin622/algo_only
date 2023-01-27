import sys

def main():
	input = sys.stdin.readline
	string = input().rstrip()
	explode = input().rstrip()
	e_len = len(explode)
	answer = []
	for s in string:
		answer.append(s)
		if s == explode[-1]:
			while ''.join(answer[-e_len:]) == explode:
				for _ in range(e_len):
					answer.pop()
	answer = ''.join(answer) if answer else 'FRULA'
	print(answer)


if __name__ == '__main__':
	main()

