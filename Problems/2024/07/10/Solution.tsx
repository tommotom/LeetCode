function minOperations(logs: string[]): number {
    let ans = 0;
    for (const l of logs) {
        if (l === "./") {
            continue;
        } else if (l === "../") {
            ans = Math.max(0, ans - 1);
        } else {
            ans++;
        }
    }
    return ans;
};
