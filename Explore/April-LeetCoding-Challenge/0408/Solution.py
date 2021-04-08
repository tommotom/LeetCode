class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        n = len(digits)
        buttons = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        ans = []

        def backtrack(arr, idx):
            nonlocal n, buttons, ans, digits

            if idx == n:
                ans.append("".join(arr))
                return

            for char in buttons[digits[idx]]:
                arr[idx] = char
                backtrack(arr, idx+1)
            return

        backtrack(["" for _ in range(n)], 0)

        return ans
