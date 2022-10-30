# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        @lru_cache(None)
        def depth(node):
            if not node: return -1
            if not node.left and not node.right: return 0
            return max(depth(node.left), depth(node.right)) + 1

        q = deque([(root,0)])
        ex = {}
        while q:
            level = q[0][1]
            line = []
            val_to_node = {}
            while q and q[0][1] == level:
                node, _ = q.popleft()
                heapq.heappush(line, (-depth(node), node.val))
                val_to_node[node.val] = node
                if node.left: q.append((node.left, level+1))
                if node.right: q.append((node.right, level+1))
            d, top = heapq.heappop(line)
            d *= -1
            ex[top] = (-line[0][0] if line else -1) + level
            while line:
                ex[heapq.heappop(line)[1]] = d + level

        return [ex[q] for q in queries]
