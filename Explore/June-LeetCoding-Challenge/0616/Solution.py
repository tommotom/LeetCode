class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1: return ["()"]
        tmp = self.generateParenthesis(n-1)
        ans = set()
        for t in tmp:
            ans.add("("+t+")")
            ans.add("()"+t)
            ans.add(t+"()")
        for num in range(2, n//2+1):
            A = self.generateParenthesis(num)
            B = self.generateParenthesis(n-num)
            for a in A:
                for b in B:
                    ans.add(a+b)
                    ans.add(b+a)
        return list(ans)