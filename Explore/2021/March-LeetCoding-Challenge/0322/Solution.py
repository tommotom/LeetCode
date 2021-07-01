class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words = {w : w for w in wordlist}
        caps = {w.lower() : w for w in wordlist[::-1]}
        vowels = {re.sub("[aiueo]", "#", w.lower()) : w for w in wordlist[::-1]}
        return [words.get(w) or caps.get(w.lower()) or vowels.get(re.sub("[aiueo]", "#", w.lower())) or "" for w in queries]
