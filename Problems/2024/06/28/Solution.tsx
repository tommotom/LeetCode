function maximumImportance(n: number, roads: number[][]): number {
    const degrees = Array(n).fill(0);
    for (const [u, v] of roads) {
        degrees[u]++;
        degrees[v]++;
    }
    degrees.sort((a, b) => a - b);

    let ans = 0;
    for (let i = 1; i <= n; i++) {
        ans += degrees[i-1] * i;
    }

    return ans;
};
