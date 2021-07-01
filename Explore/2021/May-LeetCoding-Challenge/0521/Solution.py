class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            dic1, dic2 = {}, {}
            for i in range(len(pattern)):
                if word[i] in dic1 and pattern[i] in dic2:
                    if dic1[word[i]] != pattern[i]:
                        break
                    if dic2[pattern[i]] != word[i]:
                        break
                elif word[i] in dic1 or pattern[i] in dic2:
                    break
                else:
                    dic1[word[i]] = pattern[i]
                    dic2[pattern[i]] = word[i]
            else:
                ans.append(word)
        return ans
