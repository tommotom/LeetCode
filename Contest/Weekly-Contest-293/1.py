class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        def isAnagram(w1, w2):
            if len(w1) != len(w2): return False

            counter = defaultdict(int)
            for c in w1:
                counter[c] += 1
            for c in w2:
                counter[c] -= 1

            return all(v == 0 for v in counter.values())

        i = 1
        while i < len(words):
            if isAnagram(words[i-1], words[i]):
                words.pop(i)
            else:
                i += 1
        return words
