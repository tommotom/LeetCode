class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        dic = {k: i for i, k in enumerate(req_skills)}
        def person_to_num(person):
            nonlocal dic
            ret = 0
            for skill in person:
                ret |= (1 << dic[skill])
            return ret

        people = [(person_to_num(p), i) for i, p in enumerate(people) if person_to_num(p) > 0]
        target = pow(2, len(req_skills)) - 1

        for i in range(1, len(req_skills)+1):
            for comb in itertools.combinations(people, i):
                num = 0
                for p in comb:
                    num |= p[0]
                if num == target:
                    return [p[1] for p in comb]
        return []
