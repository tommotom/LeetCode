function maxChunksToSorted(arr: number[]): number {
    const mins = [...arr], maxs = [...arr];
    const n = arr.length;
    for (let i = 1; i < n; i++) {
        maxs[i] = Math.max(maxs[i], maxs[i-1]);
    }
    for (let i = n-2; i >= 0; i--) {
        mins[i] = Math.min(mins[i], mins[i+1]);
    }
    let ans = 1;
    for (let i = 1; i < n; i++) {
        if (maxs[i-1] < mins[i]) {
            ans++;
        }
    }
    return ans;
};
