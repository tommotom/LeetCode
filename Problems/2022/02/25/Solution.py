class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')

        i = j = 0
        while i < len(version1) and j < len(version2):
            if int(version1[i]) > int(version2[j]): return 1
            if int(version1[i]) < int(version2[j]): return -1
            i += 1
            j += 1

        if i < len(version1):
            if all(int(v) == 0 for v in version1[i:]): return 0
            return 1

        if j < len(version2):
            if all(int(v) == 0 for v in version2[j:]): return 0
            return -1

        return 0
