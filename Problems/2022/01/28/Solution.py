class Trie:

    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Trie("")

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = Trie(w)
            node = node.children[w]
        node.isWord = True

    def search(self, word: str) -> bool:
        q = deque([(0, self.root)])
        for i, w in enumerate(word):
            while q and q[0][0] == i:
                _, node = q.popleft()
                if w == ".":
                    for child in node.children.values():
                        q.append((i+1, child))
                elif w in node.children:
                    q.append((i+1, node.children[w]))
        return any([node.isWord for _, node in q])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
