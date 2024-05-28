function equalSubstring(s: string, t: string, maxCost: number): number {
    const cost = [];
    for (let i = 0; i < s.length; i++) {
        cost.push(Math.abs(s.charCodeAt(i) - t.charCodeAt(i)));
    }
    let l = -1, cur = 0, ans = 0;
    for (let r = 0; r < s.length; r++) {
        cur += cost[r];
        while (cur > maxCost) {
            cur -= cost[++l];
        }
        ans = Math.max(ans, r - l);
    }
    return ans;
};
