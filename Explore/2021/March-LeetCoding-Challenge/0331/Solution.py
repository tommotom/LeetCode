class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        len_s, len_t = len(stamp), len(target)
        target_list = list(target)

        def isSubsequenceAt(idx):
            nonlocal target_list, stamp

            for char in stamp:
                if target_list[idx] == "?" or target_list[idx] == char:
                    idx += 1
                else:
                    break
            else:
                return True

            return False

        left = last = len_t
        ans = []
        while left > 0:
            for i in range(len_t - len_s + 1):
                if isSubsequenceAt(i):
                    ans.append(i)
                    for j in range(len_s):
                        if not target_list[i+j] == "?":
                            target_list[i+j] = "?"
                            left -= 1
                if left ==0: break
            if left == last:
                return []

            last = left

        return ans[::-1]
