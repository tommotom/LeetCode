function wordBreak(s: string, wordDict: string[]): string[] {
    const wordSet = new Set(wordDict);
    const ans = [];
    const helper = (i, j, arr) => {
        if (i === s.length && j === s.length+1) {
            ans.push(arr.join(' '));
            return;
        }
        if (j === s.length+1) {
            return;
        }
        if (wordSet.has(s.substring(i, j))) {
            arr.push(s.substring(i, j));
            helper(j, j+1, arr);
            arr.pop();
        }
        helper(i, j+1, arr);
    }
    helper(0, 1, []);
    return ans;
};
