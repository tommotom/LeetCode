function appendCharacters(s: string, t: string): number {
    let i = 0, j = 0, ans = 0;
    for (let j = 0; j < t.length; j++) {
        while (i < s.length && s.charAt(i) !== t.charAt(j)) {
            i++;
        }
        if (i < s.length && s.charAt(i) === t.charAt(j)) {
            i++;
        } else {
            ans++;
        }
    }
    return ans;
};
