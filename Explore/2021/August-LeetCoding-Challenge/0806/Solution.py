"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        q, ans = deque([(root, 0)]), []
        while q:
            target = q[0][1]
            tmp = []
            while q and q[0][1] == target:
                node, level = q.popleft()
                tmp.append(node.val)
                for child in node.children:
                    q.append((child, level+1))
            ans.append(tmp)
        return ans
