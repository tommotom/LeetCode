class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        low, up = int(left), int(right)

        def isValid(x: int) -> bool:
            nonlocal low, up

            if not low <= x <= up:
                return False

            x = str(x)
            return x == x[::-1]

        superpalindromes = set()
        num = 1
        while True:
            str_num = str(num)

            square1 = int(str_num + str_num[::-1]) ** 2
            if isValid(square1):
                superpalindromes.add(square1)

            square2 = int(str_num[:-1] + str_num[::-1]) ** 2
            if isValid(square2):
                superpalindromes.add(square2)
            elif square2 > up: break

            num += 1

        return len(superpalindromes)
