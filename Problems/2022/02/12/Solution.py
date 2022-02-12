from string import ascii_lowercase

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def neighbors(word):
            wordList = list(word)
            ret = []
            for i in range(len(word)):
                org = word[i]
                for c in ascii_lowercase:
                    if c == word[i]: continue
                    wordList[i] = c
                    ret.append("".join(wordList))
                wordList[i] = org
            return ret


        beginSet = set([beginWord])
        endSet = set([endWord])
        wordSet = set(wordList)

        if not endWord in wordSet: return 0
        wordSet.remove(endWord)

        ans = 1
        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet

            newSet = set()
            for b in beginSet:
                for neigh in neighbors(b):
                    if neigh in endSet: return ans + 1
                    if not neigh in wordSet: continue
                    wordSet.remove(neigh)
                    newSet.add(neigh)
            ans += 1
            beginSet = newSet

        return 0
