class Trie:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.count = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Trie("")
        for word in words:
            node = root
            for c in word:
                if not c in node.children:
                    node.children[c] = Trie(c)
                node = node.children[c]
                node.count += 1

        ans = []
        for word in words:
            count = 0
            node = root
            for c in word:
                node = node.children[c]
                count += node.count
            ans.append(count)

        return ans
