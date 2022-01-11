class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a)-1, len(b)-1
        c = 0
        arr = []

        while i >= 0 and j >= 0:
            c += 1 if a[i] == "1" else 0
            c += 1 if b[j] == "1" else 0
            arr.append(c%2)
            c //= 2
            i -= 1
            j -= 1

        while i >= 0:
            c += 1 if a[i] == "1" else 0
            arr.append(c%2)
            c //= 2
            i -= 1

        while j >= 0:
            c += 1 if b[j] == "1" else 0
            arr.append(c%2)
            c //= 2
            j -= 1

        if c > 0:
            arr.append(c)

        return "".join(map(str,arr[::-1]))
