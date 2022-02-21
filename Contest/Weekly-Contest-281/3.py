class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        alphas = [0 for _ in range(26)]
        for c in s:
            alphas[ord(c)-ord('a')] += 1

        builder = []

        i = 25
        isMax = True
        last = ''
        while i >= 0:
            if alphas[i] > 0 and i != last:
                last = i
                if not isMax:
                    builder.append(chr(i+ord('a')))
                    alphas[i] -= 1
                    i = 25
                    isMax = True
                    continue

                if alphas[i] > repeatLimit:
                    isMax = False
                    for _ in range(repeatLimit):
                        builder.append(chr(i+ord('a')))
                    alphas[i] -= repeatLimit
                    i = 25
                else:
                    for _ in range(alphas[i]):
                        builder.append(chr(i+ord('a')))
                    alphas[i] = 0
                    isMax = True
                    i = 25
            i -= 1

        return ''.join(builder)
