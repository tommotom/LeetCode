from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        length = len(beginWord)
        q = deque([(beginWord, 1)])
        visited = set([beginWord])

        def oneLetter(word1, word2):
            nonlocal length
            onlyOne = False
            for i in range(length):
                if word1[i] != word2[i]:
                    if onlyOne: return False
                    onlyOne = True
            return onlyOne

        while q:
            present, step = q.popleft()
            if present == endWord: return step

            for word in wordList:
                if word in visited: continue

                if oneLetter(present, word):
                    q.append((word, step+1))
                    visited.add(word)

        return 0
