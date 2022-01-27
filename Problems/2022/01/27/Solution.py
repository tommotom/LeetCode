class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = {}
        node = root
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                bit = (num & (1 << i)) >> i
                if bit not in node:
                    node[bit] = {}
                node = node[bit]

        ans = 0
        for num in nums:
            node = root
            tmp = 0
            for i in range(31, -1, -1):
                bit = (num & (1 << i)) >> i
                if 1 ^ bit in node:
                    tmp += 1 << i
                    node = node[1^bit]
                else:
                    node = node[bit]
            ans = max(ans, tmp)

        return ans
