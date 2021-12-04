class Node:

    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Node("")
        for word in words:
            node = self.root
            for w in word:
                if w not in node.children:
                    node.children[w] = Node(w)
                node = node.children[w]
            node.isWord = True

        self.arr = []

    def query(self, letter: str) -> bool:
        new = []

        for a in self.arr:
            if letter in a.children:
                new.append(a.children[letter])

        if letter in self.root.children:
            new.append(self.root.children[letter])

        self.arr = new

        return any(a.isWord for a in self.arr)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
