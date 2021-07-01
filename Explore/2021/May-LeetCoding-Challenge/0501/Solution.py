class Node:
    def __init__(self, idx):
        self.idx = idx
        self.children = {}

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Node(-1)
        for i, word in enumerate(words):
            for j in range(len(word)):
                node = self.trie
                for k in range(j,len(word)):
                    if word[k] not in node.children:
                        node.children[word[k]] = Node(i)
                    node = node.children[word[k]]

                if "#" not in node.children:
                    node.children["#"] = Node(-1)
                node = node.children["#"]

                for w in word:
                    if w not in node.children:
                        node.children[w] = Node(i)
                    node = node.children[w]
                    node.idx = max(node.idx, i)
        return

    def f(self, prefix: str, suffix: str) -> int:
        node = self.trie
        for s in suffix:
            if s not in node.children: return -1
            node = node.children[s]
        if "#" not in node.children: return -1
        node = node.children["#"]
        for p in prefix:
            if p not in node.children: return -1
            node = node.children[p]
        return node.idx


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
