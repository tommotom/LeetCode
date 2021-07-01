# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False

        rabbit = head
        turtle = head

        while rabbit.next and rabbit.next.next:
            rabbit = rabbit.next
            if rabbit == turtle: return True
            rabbit = rabbit.next
            if rabbit == turtle: return True
            turtle = turtle.next
        return False
