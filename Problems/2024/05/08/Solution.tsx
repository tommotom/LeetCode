function findRelativeRanks(score: number[]): string[] {
    const arr = score.map((v, i) => [v, i]).sort((a, b) => b[0] - a[0]);
    const ans = Array(score.length);
    let rank = 1;
    for (const [v, i] of arr) {
        if (rank === 1) {
            ans[i] = 'Gold Medal';
        } else if (rank === 2) {
            ans[i] = 'Silver Medal';
        } else if (rank === 3) {
            ans[i] = 'Bronze Medal';
        } else {
            ans[i] = rank.toString();
        }
        rank++;
    }
    return ans;
};
