class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        stack = []
        i1 = i2 = 0
        while i2 < n:
            if i1 < n and pushed[i1] == popped[i2]:
                i1 += 1
                i2 += 1
            elif stack and stack[-1] == popped[i2]:
                stack.pop()
                i2 += 1
            elif i1 < n:
                while i1 < n and pushed[i1] != popped[i2]:
                    stack.append(pushed[i1])
                    i1 += 1
            else: return False
        return True
