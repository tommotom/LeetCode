class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []

        root = Node()
        for word in words:
            node = root
            for i in word:
                if i not in node.children:
                    node.children[i] = Node()
                node = node.children[i]
            node.isWord = True

        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, root, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(board, node, i+1, j, path+tmp, res)
        self.dfs(board, node, i-1, j, path+tmp, res)
        self.dfs(board, node, i, j-1, path+tmp, res)
        self.dfs(board, node, i, j+1, path+tmp, res)
        board[i][j] = tmp


class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False
