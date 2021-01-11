# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head

        length = 0
        node = head
        while node:
            node = node.next
            length += 1

        if k > length // 2:
            k  = length - k + 1

        if length == k * 2 - 1: return head

        if k == 1 and length == 2:
            return self.swapNeighborHead(head, k, length)
        elif k == length - k:
            return self.swapNeighbor(head, k, length)
        elif k == 1:
            return self.swapHead(head, k, length)
        else:
            return self.swap(head, k, length)

    def swap(self, head, k, length):
        prevA = head
        for _ in range(k - 2):
            prevA = prevA.next
        A = prevA.next
        nextA = prevA.next.next if prevA.next and prevA.next.next else None

        prevB = head
        for _ in range(length - k - 1):
            prevB = prevB.next
        B = prevB.next
        nextB = prevB.next.next if prevB.next and prevB.next.next else None

        prevA.next = B
        A.next = nextB

        prevB.next = A
        B.next = nextA

        return head

    def swapNeighbor(self, head, k, length):
        prevA = head
        for _ in range(k-2):
            prevA = prevA.next
        A = prevA.next
        if not A.next: return head
        B = A.next

        prevA.next = B
        tmp = B.next
        B.next = A
        A.next = tmp

        return head

    def swapHead(self, head, k, length):
        prevTail = head
        while prevTail.next.next:
            prevTail = prevTail.next
        tail = prevTail.next

        tail.next = head.next
        prevTail.next = head
        head.next = None

        return tail

    def swapNeighborHead(self, head, k, length):
        tail = head.next
        tail.next = head
        head.next = None

        return tail
