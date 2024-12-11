import sys

class Node:
    def __init__(self, key, data=None):
        self.key = key  # key 값으로 입력될 문자
        self.data = data  # 문자열의 종료를 알리는 flag
        self.children = {}  # 자식 노드를 저장

class Trie:
    def __init__(self):
        self.head = Node(None)  # head를 빈 노드로 설정

    def insert(self, string):  # 트리를 생성하기 위한 함수
        current_node = self.head

        for char in string:  # 입력될 문자열을 하나씩 확인 후 children에 저장
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]

            if current_node.data is not None:  # 한글자씩 중간에 넣는 과정에서 지금까지의 번호로 끝나는 게 있다면 일관성 X
                                               # 짧은 번호를 먼저 순회하고 긴 번호를 순회했을 때 확인 절차
                return False

        if current_node.children:  # 다 순회 했는데 자식 노드가 더 있으면 이것도 일관성 X
                                   # 긴 번호를 먼저 순회하고 긴 번호를 순회했을 때 확인 절차
            return False

        current_node.data = string  # 문자열 다 순회하면 마지막 노드의 data에 문자열 저장. 일관성 O
        return True

##################################################################################################################
test_case = int(sys.stdin.readline())

for _ in range(test_case):
    n = int(sys.stdin.readline())
    phone_numbers = []
    trie = Trie()
    for _ in range(n):
        phone_numbers.append(sys.stdin.readline().strip())  # strip() 사용하여 양쪽 공백과 줄바꿈 표시 삭제
    TF = True

    for phone_number in phone_numbers:
        if not trie.insert(phone_number):
            TF = False
            break

    if TF:
        print('YES')
    else:
        print('NO')
