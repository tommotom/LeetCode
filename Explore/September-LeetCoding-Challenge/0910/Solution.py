from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_count = Counter(secret)
        guess_count = Counter(guess)

        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                secret_count[secret[i]] -= 1
                guess_count[secret[i]] -= 1

        cows = 0
        for k, v in guess_count.items():
            if k in secret_count:
                cows += min(secret_count[k], guess_count[k])

        return str(bulls) + 'A' + str(cows) + 'B'
