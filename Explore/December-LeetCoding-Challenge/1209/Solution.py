# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.nums = self.inorderTraversal()
        self.length = len(self.nums)
        self.idx = -1

    def next(self) -> int:
        if not self.hasNext(): return
        self.idx += 1
        return self.nums[self.idx]

    def hasNext(self) -> bool:
        return self.idx + 1 < self.length

    def inorderTraversal(self):
        stack = []
        ret = []
        node = self.root
        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                if not stack: break
                node = stack.pop()
                ret.append(node.val)
                node = node.right

        return ret



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()