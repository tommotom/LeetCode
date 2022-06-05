class Node:

    def __init__(self, c):
        self.c = c
        self.left = None
        self.right = None

class TextEditor:

    def __init__(self):
        self.cur = Node("")

    def addText(self, text: str) -> None:
        if not self.cur.left:
            node = Node(text[0])
            node.right = self.cur
            self.cur.left = node
            text = text[1:]

        left = self.cur.left
        for t in text:
            node = Node(t)
            left.right = node
            node.left = left
            node.right = self.cur
            self.cur.left = node
            left = node

    def deleteText(self, k: int) -> int:
        deleted = 0
        for _ in range(k):
            if not self.cur.left: break
            self.cur.left = self.cur.left.left
            deleted += 1
        return deleted

    def cursorLeft(self, k: int) -> str:
        for _ in range(k):
            if not self.cur.left: break
            l, r = self.cur.left, self.cur.right
            l.right = r
            if r:
                r.left = l

            tmp = l.left
            if tmp:
                tmp.right = self.cur
            self.cur.left = tmp

            l.left = self.cur
            self.cur.right = l
        return self.leftText()

    def cursorRight(self, k: int) -> str:
        for _ in range(k):
            if not self.cur.right: break
            l, r = self.cur.left, self.cur.right
            r.left = l
            if l:
                l.right = r

            tmp = r.right
            if tmp:
                tmp.left = self.cur
            self.cur.right = tmp

            r.right = self.cur
            self.cur.left = r
        return self.leftText()

    def leftText(self) -> str:
        ret = []
        node = self.cur
        for _ in range(10):
            node = node.left
            if not node: break
            ret.append(node.c)
        return "".join(ret[::-1])



# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
