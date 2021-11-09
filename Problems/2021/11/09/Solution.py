from string import ascii_lowercase

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        valid_words = defaultdict(lambda :defaultdict(int))
        for word in words:
            tmp = "".join(sorted(list(set(word))))
            if len(tmp) > 7: continue

            for c in ascii_lowercase:
                if c in tmp:
                    valid_words[c][tmp] += 1

        ans = []
        for puzzle in puzzles:
            count = 0
            head = puzzle[0]
            puzzle = sorted(puzzle)
            for bit in range(1, pow(2, 7)):
                tmp = "".join([puzzle[i] for i in range(7) if (1 << i) & bit])
                if tmp in valid_words[head]:
                    count += valid_words[head][tmp]
            ans.append(count)

        return ans
