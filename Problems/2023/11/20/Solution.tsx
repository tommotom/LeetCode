function garbageCollection(garbage: string[], travel: number[]): number {
    const counts = [];
    for (const g of garbage) {
        const count = new Map();
        for (const c of g) {
            if (!count.has(c)) {
                count.set(c, 0);
            }
            count.set(c, count.get(c) + 1);
        }
        counts.push(count);
    }

    let ans = 0;
    const type = ["G", "P", "M"];
    for (const g of type) {
        let cum = 0;
        for (let i = 0; i < counts.length; i++) {
            if (counts[i].has(g)) {
                ans += cum + counts[i].get(g);
                cum = 0;
            }
            cum += travel[i];
        }
    }

    return ans;
};
