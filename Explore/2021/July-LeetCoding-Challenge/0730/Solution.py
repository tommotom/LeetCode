class Trie:
    def __init__(self, val):
        self.val = val
        self.children = {}

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie(0)

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for w in key:
            if not w in node.children:
                node.children[w] = Trie(0)
            node = node.children[w]
        node.val = val

    def sum(self, prefix: str) -> int:
        node = self.root
        for p in prefix:
            if not p in node.children: return 0
            node = node.children[p]

        return self.dfs(node)

    def dfs(self, node):
        children = 0
        for n in node.children.values():
            children += self.dfs(n)
        return children + node.val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
