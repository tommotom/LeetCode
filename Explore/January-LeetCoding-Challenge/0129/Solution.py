from collections import deque
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root: return
        dic = defaultdict(list)

        leftmost = 0
        rightmost = 0

        q = deque([(root, 0, 0)])

        while q:
            node, x, y = q.popleft()
            leftmost = min(leftmost, x)
            rightmost = max(rightmost, x)

            while y >= len(dic[x]): dic[x].append([])

            dic[x][y].append(node.val)

            if node.left: q.append((node.left, x-1, y+1))
            if node.right: q.append((node.right, x+1, y+1))

        ans = [[] for _ in range(rightmost - leftmost + 1)]
        for x, arr in dic.items():
            for a in arr:
                for num in sorted(a):
                    ans[x - leftmost].append(num)
        return ans
