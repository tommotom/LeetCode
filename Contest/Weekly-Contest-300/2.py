# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        ans = [[-1]*n for _ in range(m)]
        i, j, h, d = 0, 0, 0, 0
        while head:
            ans[i][j] = head.val
            head = head.next
            if not head: break

            next_i = i + dirs[d][0]
            next_j = j + dirs[d][1]
            while not (0 <= next_i < m and 0 <= next_j < n and ans[next_i][next_j] == -1):
                d = (d+1) % 4
                next_i = i + dirs[d][0]
                next_j = j + dirs[d][1]
            i = next_i
            j = next_j

        return ans
