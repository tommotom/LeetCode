class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(reverse=True)
        max_attack, max_def = properties[0]
        last_attack, cur_def = max_attack, max_def

        ans = 0
        for attack, defence in properties[1:]:
            if attack < last_attack:
                max_def = cur_def
                max_attack = attack+1
            if attack < max_attack and defence < max_def:
                ans += 1
            cur_def = max(cur_def, defence)
            last_attack = attack

        return ans
