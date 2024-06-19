function minDays(bloomDay: number[], m: number, k: number): number {

    const helper = (mid) => {
        let bouquets = 0, count = 0;
        for (const b of bloomDay) {
            if (b <= mid) {
                count++;
            } else {
                count = 0;
            }
            if (count === k) {
                bouquets++;
                count = 0;
            }
        }
        return bouquets;
    }

    let l = 1, r = bloomDay.reduce((a, b) => Math.max(a, b));
    while (l < r) {
        const mid = l + Math.floor((r - l) / 2);
        if (helper(mid) < m) {
            l = mid + 1;
        } else {
            r = mid;
        }
    }
    return helper(l) >= m ? l : -1;
};
