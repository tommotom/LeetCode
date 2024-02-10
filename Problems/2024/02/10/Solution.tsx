function countSubstrings(s: string): number {
    let ans = 0;
    for (let i = 0; i < s.length; i++) {
        ans++;
        let j = 1;
        while (i - j >= 0 && i + j < s.length && s.charAt(i-j) === s.charAt(i+j)) {
            ans++;
            j++;
        }
    }
    for (let i = 1; i < s.length; i++) {
        let j = 1;
        while (i - j >= 0 && i + j - 1 < s.length && s.charAt(i-j) === s.charAt(i+j-1)) {
            ans++;
            j++;
        }
    }
    return ans;
};
