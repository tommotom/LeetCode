# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        groups = []
        lengthes = []
        tailes = []
        target = 1
        node = head
        while node:
            h = node
            length = 1
            while node and length < target:
                node = node.next
                if node: length += 1
            tailes.append(node)
            if node:
                tmp = node.next
                node.next = None
                node = tmp
            groups.append(h)
            lengthes.append(length)
            target += 1

        def reverse(head):
            if not head: return

            ret_head = head
            while head.next:
                new_head = head.next
                tmp = new_head.next
                new_head.next = ret_head
                ret_head = new_head
                head.next = tmp

            return ret_head, head


        for i, length in enumerate(lengthes):
            if length % 2 == 0:
                groups[i], tailes[i] = reverse(groups[i])

        for i in range(len(groups)-1):
            tailes[i].next = groups[i+1]
        return groups[0]
