function finalPrices(prices: number[]): number[] {
    const st = [];
    const ans = [...prices];
    for (let i = 0; i < prices.length; i++) {
        while (st.length > 0 && prices[i] <= prices[st[st.length-1]]) {
            const j = st.pop();
            ans[j] -= prices[i];
        }
        st.push(i);
    }
    return ans;
};
