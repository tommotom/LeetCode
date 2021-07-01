class Trie:
    def __init__(self, char: str):
        self.char = char
        self.isWord = False
        self.children = [None] * 26

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie("")
        for p in products:
            node = root
            for c in p:
                idx = ord(c) - ord("a")
                if not node.children[idx]:
                    node.children[idx] = Trie(c)
                node = node.children[idx]
            node.isWord = True

        ans = []
        node = root
        for i, w in enumerate(searchWord):
            idx = ord(w) - ord("a")
            if not node or not node.children[idx]:
                node = None
                ans.append([])
            else:
                node = node.children[idx]
                tmp = node
                ret = []
                stack = [(tmp, "")]
                while stack and len(ret) < 3:
                    t, path = stack.pop()
                    if t.isWord:
                        ret.append(searchWord[:i] + path+t.char)
                    for c in t.children[::-1]:
                        if c:
                            stack.append((c, path+t.char))
                ans.append(ret)
        return ans
