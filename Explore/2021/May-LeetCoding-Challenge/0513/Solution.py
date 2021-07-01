class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        ans = []
        s = s[1:len(s)-1]

        def helper(char_a, char_b):
            parse_a = parse(char_a)
            parse_b = parse(char_b)
            for a in parse_a:
                for b in parse_b:
                    ans.append('(' + a + ', ' + b + ')')

        def parse(char):
            if len(char) == 1:
                return [char]
            ret = []
            if char[0] == '0':
                if char[-1] != '0':
                    ret.append(char[0] + '.' + char[1:])
            else:
                if char[-1] != '0':
                    for i in range(1, len(char)):
                        ret.append(char[:i] + '.' + char[i:])
                ret.append(char)
            return ret

        for i in range(1, len(s)):
            helper(s[:i], s[i:])

        return ans
