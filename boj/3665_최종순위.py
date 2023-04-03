import sys
from collections import deque


def main():
    input = sys.stdin.readline
    T = int(input())
    for tc in range(T):
        n = int(input())
        in_degree = [0] * (n + 1)
        connections = [[0] * (n + 1) for _ in range(n + 1)]
        t = list(map(int, input().split()))
        for i in range(n - 1):
            for j in range(i + 1, n):
                first = t[i]
                second = t[j]
                connections[first][second] = 1
                in_degree[second] += 1
        m = int(input())
        for _ in range(m):
            a, b = map(int, input().split())
            if connections[b][a]:
                in_degree[a] -= 1
                in_degree[b] += 1
                connections[b][a] = 0
                connections[a][b] = 1
            else:
                in_degree[b] -= 1
                in_degree[a] += 1
                connections[a][b] = 0
                connections[b][a] = 1
        answer = []
        queue = deque()
        for i in range(1, n + 1):
            if in_degree[i] == 0:
                queue.append(i)
        is_answer_found = False
        while queue:
            if len(queue) > 1:
                is_answer_found = True
                print("?")
                break
            node = queue.popleft()
            answer.append(node)
            if len(answer) == n:
                is_answer_found = True
                print(*answer)
                break
            for i in range(1, n + 1):
                if connections[node][i]:
                    connections[node][i] = 0
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        queue.append(i)
                    elif in_degree[i] < 0:
                        queue.clear()
                        break
        if not is_answer_found:
            print("IMPOSSIBLE")


if __name__ == "__main__":
    main()
