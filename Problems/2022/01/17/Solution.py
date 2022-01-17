class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        key_to_word = {}
        word_to_key = {}

        if len(pattern) != len(arr): return False

        for i in range(len(pattern)):
            key, word = pattern[i], arr[i]
            if key in key_to_word and key_to_word[key] != word: return False
            if word in word_to_key and word_to_key[word] != key: return False
            key_to_word[key] = word
            word_to_key[word] = key

        return True
