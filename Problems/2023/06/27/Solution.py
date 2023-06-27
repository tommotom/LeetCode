class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        q = [(nums1[0]+nums2[0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        ans = []
        for _ in range(k):
            if not q: break
            s, l, r = heapq.heappop(q)
            ans.append([nums1[l], nums2[r]])
            if l + 1 < len(nums1) and (l+1, r) not in visited:
                visited.add((l+1, r))
                heapq.heappush(q, (nums1[l+1]+nums2[r], l+1, r))
            if r + 1 < len(nums2) and (l, r+1) not in visited:
                visited.add((l, r+1))
                heapq.heappush(q, (nums1[l]+nums2[r+1], l, r+1))
        return ans
