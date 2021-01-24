class Solution:
    def maximumTime(self, time: str) -> str:
        digits = {"4", "5", "6", "7", "8", "9"}

        ans = ""

        if time[0] == "?":
            if time[1] in digits: ans += "1"
            else: ans += "2"
        else: ans += time[0]

        if time[1] == "?":
            if ans[0] == "2": ans += "3"
            else: ans += "9"
        else: ans += time[1]

        ans += ":"

        if time[3] == "?": ans += "5"
        else: ans += time[3]

        if time[4] == "?": ans += "9"
        else: ans += time[4]

        return ans
