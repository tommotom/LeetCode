class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dic = {c:i+1 for i, c in enumerate(order)}
        def calc(word):
            nonlocal order_dic
            num = 0
            for i, c in enumerate(word):
                num += 26 ** (-i) * order_dic[c]
            return num

        return words == sorted(words, key=lambda x: calc(x))
