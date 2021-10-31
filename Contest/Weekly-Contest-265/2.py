# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next

        isCritical = [False for _ in range(len(arr))]
        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                isCritical[i] = True
            if arr[i-1] > arr[i] and arr[i] < arr[i+1]:
                isCritical[i] = True

        if len([i for i in range(len(isCritical)) if isCritical[i] == True]) < 2: return [-1, -1]

        first, last = -1, -1
        ans = [float('inf'), -float('inf')]
        for i in range(len(arr)):
            if isCritical[i] == True:
                if first == -1:
                    first = i
                if last != -1:
                    ans[0] = min(ans[0], i - last)
                last = i
        ans[1] = last - first

        return ans
