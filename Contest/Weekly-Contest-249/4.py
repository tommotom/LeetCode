# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        nodes, degs = {}, defaultdict(int)
        for t in trees:
            degs[t.val]
            if t.left:
                degs[t.left.val] += 1
                if not t.left.val in nodes: nodes[t.left.val] = t.left
            if t.right:
                degs[t.right.val] += 1
                if not t.right.val in nodes: nodes[t.right.val] = t.right
            nodes[t.val] = t

        sources = [val for val, deg in degs.items() if deg == 0]
        if len(sources) != 1: return None

        visited = set()
        invalid = False
        cur = -float('inf')
        def inorder(val):
            nonlocal visited, invalid, cur
            if val in visited:
                invalid = True
                return
            visited.add(val)
            node = nodes[val]
            if node.left:
                node.left = inorder(node.left.val)
            if val <= cur:
                invalid = True
                return
            cur = val
            if node.right:
                node.right = inorder(node.right.val)
            return node
        ans = inorder(sources[0])
        if len(visited) != len(nodes) or invalid: return None
        return ans
