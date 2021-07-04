class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        unit = 1 << 17
        mod = (1 << 128) - 159

        def rabinKarp(path, length):
            nonlocal unit, mod
            maxDigit = (1 << ((length-1) * 17)) % mod

            hashVal = 0
            for i in range(length):
                hashVal *= unit
                hashVal += path[i]
                hashVal %= mod

            allHashes = set([hashVal])
            for i in range(len(path) - length):
                hashVal -= maxDigit * path[i]
                hashVal *= unit
                hashVal += path[i+length]
                hashVal %= mod
                allHashes.add(hashVal)

            return allHashes

        l, r = 0, min(len(path) for path in paths) + 1
        while l+1 < r:
            m = (l + r) // 2
            common = rabinKarp(paths[0], m)
            for i in range(1, len(paths)):
                common &= rabinKarp(paths[i], m)
            if not common:
                r = m
            else:
                l = m
        return l
