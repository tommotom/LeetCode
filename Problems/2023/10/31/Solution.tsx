function findArray(pref: number[]): number[] {
    const ans = [pref[0]];
    let cum = pref[0]
    for (const num of pref.slice(1, pref.length)) {
        ans.push(num ^ cum);
        cum ^= ans[ans.length-1];
    }
    return ans;
};
