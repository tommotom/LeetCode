class Solution:
    def largestPalindromic(self, num: str) -> str:
        counter = Counter(list(num))
        arr = []
        can = "987654321"
        last = -1
        while len(arr) > last:
            last = len(arr)
            for n in can:
                if counter[n] > 1:
                    arr.append(n)
                    counter[n] -= 2
                    break
            else:
                if len(arr) > 0 and counter["0"] > 1:
                    arr.append("0")
                    counter["0"] -= 2

        for n in can:
            if counter[n] > 0:
                return "".join(arr + [n] + arr[::-1])

        if counter["0"] > 0:
            return "".join(arr + ["0"] + arr[::-1])

        return "".join(arr + arr[::-1])
