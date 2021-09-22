class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [word for word in arr if len(set(word)) == len(word)]

        ans = 0

        def helper(i, unique):
            nonlocal ans, arr
            if i == len(arr):
                ans = max(ans, len(unique))
                return

            for w in arr[i]:
                if w in unique: break
            else:
                for w in arr[i]:
                    unique.add(w)
                helper(i+1, unique)
                for w in arr[i]:
                    unique.remove(w)

            helper(i+1, unique)

        helper(0, set())

        return ans
