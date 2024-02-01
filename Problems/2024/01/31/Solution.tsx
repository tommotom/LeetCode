function dailyTemperatures(temperatures: number[]): number[] {
    const st = [], ans = Array(temperatures.length).fill(0);
    for (let i = 0; i < temperatures.length; i++) {
        while (st.length > 0 && temperatures[i] > temperatures[st[st.length-1]]) {
            const j = st.pop();
            ans[j] = i - j;
        }
        st.push(i);
    }
    return ans;
};
