class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        for a, b in queries:
            tmp = 1
            while a != b:
                tmp += 1
                if a > b:
                    a //= 2
                else:
                    b //= 2
            ans.append(tmp)

        return ans
