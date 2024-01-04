import sys


def dfs(here: int):
    # 삭제할 노드가 루트 노드인 경우, 트리에는 노드가 없으므로 0을 반환
    if here == delete_node:
        return 0

    # 자식 노드가 없거나 모든 자식 노드가 삭제된 경우, 현재 노드는 리프 노드
    if len(tree[here]) == 0 or all(child == delete_node for child in tree[here]):
        return 1

    result = 0
    for there in tree[here]:
        if there != delete_node:
            result += dfs(there)

    return result

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    parents = list(map(int, sys.stdin.readline().split()))
    delete_node = int(sys.stdin.readline().strip())

    tree = [[] for _ in range(N)]
    root = 0
    for idx, p in enumerate(parents):
        if p == -1:
            root = idx
        else:
            tree[p].append(idx)

    # 삭제할 노드가 루트 노드인 경우를 처리
    if delete_node == root:
        print(0)
    else:
        print(dfs(root))