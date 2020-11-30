class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return

        def helper(l, r):
            if l == r: return [[buildings[l][0], buildings[l][2]], [buildings[l][1], 0]]

            m = (l + r) // 2
            left = helper(l, m)
            right = helper(m+1, r)

            lp = rp = 0
            lh = rh = 0
            ret = []
            while lp < len(left) and rp < len(right):
                if left[lp][0] < right[rp][0]:
                    if not rh or rh < left[lp][1]:
                        ret.append(left[lp])
                    elif lh and lh > rh:
                        ret.append([left[lp][0], rh])
                    lh = left[lp][1]
                    lp += 1
                elif left[lp][0] > right[rp][0]:
                    if not lh or lh < right[rp][1]:
                        ret.append(right[rp])
                    elif rh and rh > lh:
                        ret.append([right[rp][0], lh])
                    rh = right[rp][1]
                    rp += 1
                else:
                    height = max(left[lp][1], right[rp][1])
                    if not ret or ret and ret[-1][-1] != height:
                        ret.append([left[lp][0], height])
                    lh, rh = left[lp][1], right[rp][1]
                    lp += 1
                    rp += 1

            return ret + left[lp:] + right[rp:]

        return helper(0, len(buildings)-1)
            