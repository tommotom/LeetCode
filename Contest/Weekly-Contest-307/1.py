class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ans = 0
        for ex, en in zip(experience, energy):
            if ex >= initialExperience:
                ans += ex - initialExperience + 1
                initialExperience += ex - initialExperience + 1
            if en >= initialEnergy:
                ans += en - initialEnergy + 1
                initialEnergy += en - initialEnergy + 1
            initialExperience += ex
            initialEnergy -= en
        return ans
