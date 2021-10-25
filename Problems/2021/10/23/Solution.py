<<<<<<< HEAD
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        max_depth = 0
        node = root
        while node:
            max_depth += 1
            node = node.left

        def has_n_nodes_at_last_row(root, n):
            depth = 1
            node = root
            took = 0
            while depth < max_depth:
                if took + pow(2, max_depth-1-depth) >= n:
                    node = node.left
                else:
                    node = node.right
                    took += pow(2, max_depth-1-depth)
                depth += 1
            return node is not None

        l, r = 1, pow(2, max_depth-1)+1
        while l < r:
            m = l + (r - l) // 2
            if has_n_nodes_at_last_row(root, m):
                l = m + 1
            else:
                r = m

        return pow(2, max_depth-1) + l-2
=======
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r-l) // 2
            if nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r -= 1
        return nums[l]
>>>>>>> f7b18ebd954cd1b5e117dccf515afa0efa072d6a
