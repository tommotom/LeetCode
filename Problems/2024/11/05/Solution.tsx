function minChanges(s: string): number {
    let ans = 0;
    for (let i = 0; i < s.length; i += 2) {
        if (s.charAt(i) !== s.charAt(i+1)) {
            ans++;
        }
    }
    return ans;
};
