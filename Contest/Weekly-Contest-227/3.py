class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        def word1IsBetter(i, j):
            nonlocal word1, word2, len1, len2
            while i < len1 and j < len2:
                if word1[i] > word2[j]: return True
                elif word1[i] < word2[j]: return False
                i += 1
                j += 1
            if i == len1: return False
            else: return True

        merge = []
        i = j = 0
        len1, len2 = len(word1), len(word2)
        while i < len1 and j < len2:
            if word1[i] > word2[j]:
                merge.append(word1[i])
                i += 1
            elif word1[i] < word2[j]:
                merge.append(word2[j])
                j += 1
            else:
                current = word1[i]
                i2, j2 = i, j
                while i2 < len1 and j2 < len2 and word1[i2] == current and word2[j2] == current:
                    i2 += 1
                    j2 += 1

                if i2 < len1 and j2 < len2:
                    if word1[i2] < current and word2[j2] < current:
                        while i < i2:
                            merge.append(word1[i])
                            i += 1
                        while j < j2:
                            merge.append(word2[j])
                            j += 1
                    elif word1IsBetter(i, j):
                        while i < i2:
                            merge.append(word1[i])
                            i += 1
                    else:
                        while j < j2:
                            merge.append(word2[j])
                            j += 1

                elif i2 == len1:
                    while j < j2:
                        merge.append(word2[j])
                        j += 1
                else:
                    while i < i2:
                        merge.append(word1[i])
                        i += 1

        while i < len1:
            merge.append(word1[i])
            i += 1

        while j < len2:
            merge.append(word2[j])
            j += 1

        return "".join(merge)

