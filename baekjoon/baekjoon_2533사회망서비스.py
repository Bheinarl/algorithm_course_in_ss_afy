import sys
from collections import defaultdict

class Tree:
    def __init__(self, N):  # 변수 설정
        self.N = N
        self.graph = defaultdict(list)  # 기본 값을 빈 리스트로 생성
        self.dp = [[0, 0] for _ in range(N + 1)]  # dp[node][0] : 얼리어답터 아닐 때, dp[node][1] : 얼리어답터일 때

    def add_edge(self, u, v):  # 연결 되어있다는 부분 추가
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, root):  # dfs로
        stack = [(root, -1)]  # (현재 노드, 부모 노드)  # 여기서는 부모 노드가 없다는 것을 표기하기위해 -1로 설정
        order = []  # 위에서부터 순서대로 저장

        while stack:
            node, parent = stack.pop()
            order.append((node, parent))  # 트리 구조 상 위에서부터 dfs 순서대로 저장
            for child in self.graph[node]:  # 간선이 연결된, 이 문제에서는 연결된 친구
                if child != parent:  # 자기 자신을 제외한 자식 노드
                    stack.append((child, node))  # 스택에 추가

        for node, parent in reversed(order):  # 확인은 밑에서부터 dfs 역순으로 확인
            self.dp[node][0] = 0  # 해당 노드가 얼리어답터가 아닐 때
            self.dp[node][1] = 1  # 해당 노드가 얼리어답터라서 얼리어답터 인원 추가

            for child in self.graph[node]:  # 트리 구조 상 자식 노드
                if child != parent:  # 자기 자신이 아닌 자식 노드라면
                    self.dp[node][0] += self.dp[child][1]
                    # 트리 구조 상 밑에서부터 올라가고 있으니깐 자식 노드부터 스캔한 얼리어답터 인원 수 추가
                    # 내가 얼리어답터가 아니기 때문에 자식 노드는 무조건 얼리어답터여야함
                    self.dp[node][1] += min(self.dp[child][0], self.dp[child][1])
                    # 트리 구조 상 밑에서부터 올라가고 있으니깐 자식 노드부터 스캔한 얼리어답터 인원 수 추가
                    # 내가 얼리어답터이기 때문에 자식 노드는 얼리어답터여도 되고, 아니여도 됨

    def get_answer(self):
        return min(self.dp[1][0], self.dp[1][1])  # root 노드가 얼리어답터일 때, 아닐 때 중 최솟값 반환


N = int(sys.stdin.readline())
tree = Tree(N)

for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    tree.add_edge(u, v)

tree.dfs(1)
print(tree.get_answer())