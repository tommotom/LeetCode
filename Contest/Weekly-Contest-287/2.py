class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        counter = {}
        for w, l in matches:
            if w not in counter:
                counter[w] = [0, 0]
            if l not in counter:
                counter[l] = [0, 0]
            counter[w][0] += 1
            counter[l][1] += 1

        zero, one = [], []
        for i in range(1, 10**5+1):
            if i in counter:
                if counter[i][1] == 0:
                    zero.append(i)
                if counter[i][1] == 1:
                    one.append(i)

        return [zero, one]
