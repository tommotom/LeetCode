function wordBreak(s: string, wordDict: string[]): boolean {
    const wordSet: Set<string> = new Set(wordDict);
    const memo: Map<number, boolean> = new Map();

    function dfs(i: number): boolean {
        if (i === s.length) {
            return true;
        }
        if (memo.has(i)) {
            return memo.get(i);
        }
        for (let j = i+1; j <=s.length; j++) {
            if (wordSet.has(s.substring(i, j)) && dfs(j)) {
                memo.set(i, true);
                return true;
            }
        }
        memo.set(i, false);
        return false;
    }

    return dfs(0);
};
