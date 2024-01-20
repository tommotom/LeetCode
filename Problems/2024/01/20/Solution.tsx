function sumSubarrayMins(arr: number[]): number {
    const mod = 1000000007;
    let ans = 0;
    const st = [];
    for (let i = 0; i <= arr.length; i++) {
        let len = st.length
        while (len > 0 && (i === arr.length || arr[st[len-1]] >= arr[i])) {
            const m = st.pop();
            len--;
            const l = len === 0 ? -1 : st[len-1];

            ans += ((m - l) * (i - m) * arr[m]) % mod;
            ans %= mod;
        }
        st.push(i);
    }
    return ans
};
