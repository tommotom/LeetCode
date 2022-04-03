class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def helper(h, m, H, M):
            if h == H and m == M: return 0
            if 60 * h + m + 60 <= 60 * H + M:
                h += (m + 60) // 60
                m = (m + 60) % 60
            elif 60 * h + m + 15 <= 60 * H + M:
                h += (m + 15) // 60
                m = (m + 15) % 60
            elif 60 * h + m + 5 <= 60 * H + M:
                h += (m + 5) // 60
                m = (m + 5) % 60
            else:
                h += (m + 1) // 60
                m = (m + 1) % 60
            return 1 + helper(h, m, H, M)

        return helper(int(current[:2]), int(current[3:]), int(correct[:2]), int(correct[3:]))
