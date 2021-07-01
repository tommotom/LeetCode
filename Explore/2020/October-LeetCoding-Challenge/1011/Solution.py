class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        used = {k: 0 for k, v in count.items()}
        arr = []
        ans = ""
        for c in s:
            count[c] -= 1
            if used[c]: continue
            while ans and ans[-1] > c and count[ans[-1]]:
                used[ans[-1]] = 0
                ans = ans[:-1]
            ans += c
            used[c] = 1

        return ans
