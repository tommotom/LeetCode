class Solution:
    def smallestString(self, s: str) -> str:

        def helper(l, r):
            ret = []
            for c in s[l:r]:
                ret.append(chr(ord(c)-1) if c != 'a' else 'z')
            return ''.join(ret)

        l = 0
        while l+1 < len(s) and s[l] == 'a': l += 1

        r = l + 1
        while r < len(s) and s[r] != 'a': r += 1

        return s[:l] + helper(l, r) + s[r:]
