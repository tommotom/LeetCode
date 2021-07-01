class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        concatenations = set()

        for word in words:
            char = ""
            for c in word:
                char += codes[ord(c) - ord("a")]
            concatenations.add(char)

        return len(concatenations)
