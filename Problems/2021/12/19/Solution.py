class Solution:
    def decodeString(self, s: str) -> str:
        decoded = []
        i = 0
        while i < len(s):
            if s[i].isdigit():

                j = i
                while s[j].isdigit():
                    j += 1
                times = int(s[i:j])

                start = j+1
                j = start
                level = 1
                while level > 0:
                    if s[j] == '[':
                        level += 1
                    elif s[j] == ']':
                        level -= 1
                    j += 1
                decoded.append(self.decodeString(s[start:j-1]) * times)
                i = j
            else:
                decoded.append(s[i])
                i += 1
        return "".join(decoded)
