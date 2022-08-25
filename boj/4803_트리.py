import sys


def main():
    sys.setrecursionlimit(505)
    input = sys.stdin.readline
    test_case_idx = 0
    while True:
        n, m = map(int, input().split())
        if n == 0:
            return ()
        test_case_idx += 1
        connections = {i: [] for i in range(1, n + 1)}
        for _ in range(m):
            v1, v2 = sorted(map(int, input().split()))
            connections[v1].append(v2)
            connections[v2].append(v1)
        # dfs
        tree_cnt = 0
        visited = [0] * (n + 1)
        for i in range(1, n + 1):
            # dfs
            stack = [i]
            v_cnt = 0  # 정점의 개수
            e_cnt = 0  # 간선의 개수
            while stack:
                v = stack.pop()
                if not visited[v]:
                    visited[v] = 1
                    v_cnt += 1
                    for next_v in connections[v]:
                        e_cnt += 1
                        if not visited[next_v]:
                            stack.append(next_v)
            if (v_cnt - 1) * 2 == e_cnt:
                tree_cnt += 1
        if tree_cnt == 0:
            answer = "No trees."
        elif tree_cnt == 1:
            answer = "There is one tree."
        else:
            answer = f"A forest of {tree_cnt} trees."
        print(f"Case {test_case_idx}: {answer}")


if __name__ == '__main__':
    main()
