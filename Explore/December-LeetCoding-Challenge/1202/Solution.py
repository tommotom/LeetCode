from random import randrange

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.length = self.getLength()

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return self.getKthNo(randrange(self.length))

    def getLength(self):
        node = self.head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def getKthNo(self, k):
        node = self.head
        while k:
            node = node.next
            k -= 1
        return node.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
