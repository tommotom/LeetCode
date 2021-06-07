class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        f_to_t, t_to_f = {}, {}
        for num in nums:
            f_to_t[num], t_to_f[num] = num, num
            if num+1 in f_to_t:
                f_to_t[num] = f_to_t[num+1]
                t_to_f[f_to_t[num]] = num
                del f_to_t[num+1]
            if num-1 in t_to_f:
                t_to_f[num] = t_to_f[num-1]
                f_to_t[t_to_f[num]] = num
                del t_to_f[num-1]

        visited = set()
        ans = 0
        for f, t in f_to_t.items():
            if f in visited or t in visited: continue
            visited.add(f)
            visited.add(t)
            while f in t_to_f and f != t_to_f[f]:
                f = t_to_f[f]
                visited.add(f)
            while t in f_to_t and t != f_to_t[t]:
                t = f_to_t[t]
                visited.add(t)
            ans = max(ans, t-f+1)

        return ans
