function minBitFlips(start: number, goal: number): number {
    let ans = 0;
    while (start > 0 || goal > 0) {
        if (start % 2 !== goal % 2) {
            ans++;
        }
        start = Math.floor(start/2);
        goal = Math.floor(goal/2);
    }
    return ans;
};
