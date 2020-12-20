class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size = 0
        for char in S:
            if char.isdigit():
                size *= int(char)
            else:
                size += 1
        for char in S[::-1]:
            K %= size
            if K == 0 and char.isalpha():
                return char
            if char.isdigit():
                size //= int(char)
            else:
                size -= 1
        return None
