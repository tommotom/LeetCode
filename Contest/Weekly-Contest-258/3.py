class Solution:
    def maxProduct(self, s: str) -> int:
        palindromes = set()

        def find_palindrome(l, r, indices):
            nonlocal s, palindromes
            if l < 0 or r == len(s):
                palindromes.add(tuple(indices))
                return
            i = r
            while i < len(s):
                if s[l] == s[i]:
                    indices.append(l)
                    indices.append(i)
                    find_palindrome(l-1, i+1, indices)
                    indices.pop()
                    indices.pop()
                i += 1
            find_palindrome(l-1, r, indices)
        for i in range(len(s)):
            palindromes.add(tuple([i]))
            if 0 < i < len(s) - 1:
                find_palindrome(i-1, i+1, [i])
        for i in range(1, len(s)):
            find_palindrome(i-1, i, [])

        ans = 0
        palindromes = [set(palin) for palin in palindromes]
        for i in range(len(palindromes)-1):
            for j in range(i+1, len(palindromes)):
                if palindromes[i].intersection(palindromes[j]) == set():
                    ans = max(ans, len(palindromes[i]) * len(palindromes[j]))
        return ans
