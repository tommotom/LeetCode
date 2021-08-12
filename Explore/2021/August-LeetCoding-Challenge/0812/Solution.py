class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def genKey(s):
            tmp = [0 for _ in range(26)]
            for c in s:
                tmp[ord(c)-ord('a')] += 1
            return tuple(tmp)

        hashMap = defaultdict(list)
        for s in strs:
            hashMap[genKey(s)].append(s)

        return list(hashMap.values())
