class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        increment = set(["X++","++X"])
        decrement = set(["--X","X--"])
        X = 0
        for ope in operations:
            if ope in increment:
                X += 1
            elif ope in decrement:
                X -= 1
        return X
