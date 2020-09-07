class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str_list = str.split()
        if len(pattern) != len(str_list):
            return False

        dic = {}
        dic_rev = {}
        for i, v in enumerate(str_list):
            if not pattern[i] in dic:
                dic[pattern[i]] = v
            elif dic[pattern[i]] != v:
                return False

            if not v in dic_rev:
                dic_rev[v] = pattern[i]
            elif dic_rev[v] != pattern[i]:
                return False

        return True
