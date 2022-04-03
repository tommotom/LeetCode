class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.enc = {k: v for k, v in zip(keys, values)}
        self.decrypt = Counter(self.encrypt(w) for w in dictionary).__getitem__

    def encrypt(self, word1: str) -> str:
        return ''.join(self.enc[w] for w in word1)

# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
