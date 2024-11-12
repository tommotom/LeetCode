function maximumBeauty(items: number[][], queries: number[]): number[] {
    items.sort((a, b) => a[0] !== b[0] ? a[0] - b[0] : b[1] - a[1]);
    let max = 0;
    const arr = [];
    for (const [p, b] of items) {
        max = Math.max(max, b);
        if (arr.length > 0 && arr[arr.length-1][0] === p) {
            continue;
        }
        arr.push([p, max]);
    }

    const ans = [];
    for (const q of queries) {
        let l = 0, r = arr.length;
        while (l < r) {
            const m = l + Math.floor((r - l) / 2);
            if (arr[m][0] <= q) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        if (l === 0) {
            ans.push(0);
        } else {
            ans.push(arr[l-1][1]);
        }
    }

    return ans;
};
