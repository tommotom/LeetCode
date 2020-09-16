class Node:
    def __init__(self):
        self.zero = None
        self.one = None

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Node()
        nums = list(map(lambda x: format(x, '032b'), nums))
        for num in nums:
            node = root
            for digit in num:
                if digit == '0':
                    if not node.zero: node.zero = Node()
                    node = node.zero
                else:
                    if not node.one: node.one = Node()
                    node = node.one

        ans = 0
        for num in nums:
            node = root
            tmp = ''
            for i, digit in enumerate(num):
                if digit == '0':
                    if node.one:
                        tmp += '1'
                        node = node.one
                    else:
                        tmp += '0'
                        node = node.zero
                if digit == '1':
                    if node.zero:
                        tmp += '1'
                        node = node.zero
                    else:
                        tmp += '0'
                        node = node.one
            ans = max(ans, int(tmp, 2))

        return ans
