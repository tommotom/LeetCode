class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)

        def isValid(state):
            nonlocal statements, n
            isGoodPerson = [True if state & (1 << i) else False for i in range(n)]
            for i in range(n):
                if isGoodPerson[i]:
                    for j in range(n):
                        if statements[i][j] == 0:
                            if isGoodPerson[j] == True: return False
                            isGoodPerson[j] = False
                        if statements[i][j] == 1:
                            if isGoodPerson[j] == False: return False
                            isGoodPerson[j] = True

            return True

        ans = 0
        for state in range(pow(2, n)):
            if isValid(state):
                ans = max(ans, Counter(bin(state))["1"])
        return ans
