class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens = sorted(tokens)

        score = ans = 0
        i, j = 0, len(tokens) - 1
        while True:
            while i <= j and tokens[i] <= P:
                P -= tokens[i]
                score += 1
                i += 1
            ans = max(score, ans)

            if i <= j:
                if score > 0:
                    score -= 1
                    P += tokens[j]
                    j -= 1
                else:
                    break
            else:
                break

        return ans
