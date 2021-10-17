class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        last_num = -1
        for c in s:
            if c.isdigit():
                if not last_num < int(c):
                    return False
                last_num = int(c)
        return True
