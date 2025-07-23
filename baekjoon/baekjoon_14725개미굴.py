from collections import defaultdict

def get_trie():
    return defaultdict(get_trie)

def insert(trie, path):
    for food in path:
        trie = trie[food]

def dfs(trie, floor):
    for key in sorted(trie.keys()):
        print('--' * floor + key)
        dfs(trie[key], floor + 1)


N = int(input())
trie = get_trie()

for _ in range(N):
    food_info = input().split()
    insert(trie, food_info[1:])

dfs(trie, 0)