class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        seen = {}
        for i in range(len(s)):
            if s[i] == "0":
                if 0 not in seen:
                    seen[0] = [i, i]
                continue
            for j in range(i, len(s)):
                num = int(s[i:j+1], 2)
                if num > 10000000000: break
                if num not in seen:
                    seen[num] = [i, j]

        ans = []
        for first, second in queries:
            num = first ^ second
            if num in seen:
                ans.append(seen[num])
            else:
                ans.append([-1, -1])

        return ans
