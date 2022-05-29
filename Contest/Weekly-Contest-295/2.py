class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        sentence = sentence.split()
        def isAmount(s):
            if len(s) < 1: return False
            return s[0] == "$" and s[1:].isdecimal()
        def dis(s):
            return '$' +  '{:.2f}'.format(int(s[1:]) * (100-discount)/100)
        for i in range(len(sentence)):
            if isAmount(sentence[i]):
                sentence[i] = dis(sentence[i])
        return ' '.join(sentence)
