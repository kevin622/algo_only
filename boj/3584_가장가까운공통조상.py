import sys
from collections import deque


def main():
    input = sys.stdin.readline

    T = int(input())
    for tc in range(T):
        N = int(input())
        parents = [0] * (N + 1)
        children = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            parent, child = map(int, input().split())
            parents[child] = parent
            children[parent].append(child)
        root: int = -1
        for i in range(1, N + 1):
            if parents[i] == 0:
                root = i
                break
        depths = [0] * (N + 1)
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            depths[node] = depth
            for child_node in children[node]:
                queue.append((child_node, depth + 1))
        node1, node2 = map(int, input().split())
        n1, n2 = node1, node2
        d1, d2 = depths[n1], depths[n2]
        while d1 > d2:
            d1 -= 1
            n1 = parents[n1]
        while d2 > d1:
            d2 -= 1
            n2 = parents[n2]
        while n1 != n2:
            n1, n2 = parents[n1], parents[n2]
        print(n1)


if __name__ == "__main__":
    main()
