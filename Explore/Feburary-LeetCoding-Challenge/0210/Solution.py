"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return

        new_head = Node(head.val)
        dic = {head : new_head}
        node = new_head

        while head:
            if head.next:
                if head.next in dic:
                    node.next = dic[head.next]
                else:
                    node.next = Node(head.next.val)
                    dic[head.next] = node.next
            if head.random:
                if head.random in dic:
                    node.random = dic[head.random]
                else:
                    node.random = Node(head.random.val)
                    dic[head.random] = node.random
            head = head.next
            node = node.next

        return new_head
