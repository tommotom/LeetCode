class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st, res = [], 0
        for height in heights + [-1]:
            step = 0
            while st and st[-1][1] >= height:
                w, h = st.pop()
                step += w
                res = max(res, step * h)
            st.append((step+1, height))
        return res