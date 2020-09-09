class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1, version2 = version1.split('.'), version2.split('.')
        len1, len2 = len(version1), len(version2)
        idx1, idx2 = 0, 0
        while True:
            if idx1 < len1 and idx2 < len2:
                num1, num2 = int(version1[idx1]), int(version2[idx2])
                if num1 > num2: return 1
                if num1 < num2: return -1
                idx1 += 1
                idx2 += 1
            elif idx1 < len1:
                num1 = int(version1[idx1])
                if num1 > 0: return 1
                idx1 += 1
            elif idx2 < len2:
                num2 = int(version2[idx2])
                if num2 > 0: return -1
                idx2 += 1
            else:
                return 0
