class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        keys = [pressedKeys[0]]
        counts = [1]
        for key in pressedKeys[1:]:
            if keys[-1] == key:
                counts[-1] += 1
            else:
                keys.append(key)
                counts.append(1)

        three = [0, 1, 2, 4]
        four = [0, 1, 2, 4, 8]
        mod = 10 ** 9 + 7
        for i in range(4, max(counts)+1):
            three.append((three[-1] + three[-2] + three[-3])%mod)
            four.append((four[-1] + four[-2] + four[-3] + four[-4])%mod)

        ans = 1
        for i in range(len(keys)):
            ans *= four[counts[i]] if keys[i] == '7' or keys[i] == '9' else three[counts[i]]
            ans %= mod

        return ans
