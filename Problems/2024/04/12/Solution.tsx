function trap(height: number[]): number {
    const st = [];
    let ans = 0;
    for (let r = 0; r < height.length; r++) {
        while (st.length > 0 && height[st[st.length-1]] < height[r]) {
            const m = st.pop();
            if (st.length === 0) {
                break;
            }
            const l = st[st.length-1];
            const h = Math.min(height[r], height[l]) - height[m];
            const w = r - l - 1;
            ans += w * h;
        }
        st.push(r);
    }
    return ans;
};
