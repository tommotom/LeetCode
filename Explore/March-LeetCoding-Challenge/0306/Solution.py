class Trie:
    def __init__(self, char, length):
        self.char = char
        self.length = length
        self.isLeaf = False
        self.children = {}

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = Trie("", None)
        leaves = 0
        total = 0
        for word in words:
            node = root
            length = 0
            for w in reversed(word):
                length += 1
                if w not in node.children:
                    node.children[w] = Trie(w, length)
                node = node.children[w]
                if node.isLeaf:
                    node.isLeaf = False
                    leaves -= 1
                    total -= node.length
            if not node.children:
                node.isLeaf = True
                leaves += 1
                total += node.length
        return leaves + total
