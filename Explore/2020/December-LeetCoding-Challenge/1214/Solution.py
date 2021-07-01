class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def helper(arr, string):
            if not string:
                ans.append([c for c in arr])
                return

            for i in range(len(string)):
                tmp = string[:i+1]
                if tmp == tmp[::-1]:
                    arr.append(tmp)
                    helper(arr, string[i+1:])
                    arr.pop()
            return

        helper([], s)
        return ans