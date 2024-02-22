function findJudge(n: number, trust: number[][]): number {
    const trusted = Array(n).fill(0);
    const trusts = Array(n).fill(0);
    for (const [a, b] of trust) {
        trusts[a-1]++;
        trusted[b-1]++;
    }
    const judge = []
    for (let i = 0; i < n; i++) {
        if (trusted[i] === n-1 && trusts[i] === 0) {
            judge.push(i+1);
        }
    }
    return judge.length === 1 ? judge[0] : -1;
};
