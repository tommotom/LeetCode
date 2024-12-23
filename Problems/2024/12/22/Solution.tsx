function leftmostBuildingQueries(heights: number[], queries: number[][]): number[] {
    const n = heights.length;
    let tmp = 1;
    while (tmp < n) {
        tmp *= 2;
    }
    const size = tmp * 2;
    const data = Array(size).fill(0);

    const update = (k, a) => {
        let kk = (k-1)+tmp;
        data[kk] += a;
        while (kk > 1) {
            const half = Math.floor(kk/2);
            if (kk % 2 == 0) {
                data[half] = Math.max(data[kk], data[kk+1]);
            } else {
                data[half] = Math.max(data[kk], data[kk-1]);
            }
            kk = half;
        }
    }

    const query = (left, right) => {
        let l = (left-1) + tmp;
        let r = (right-1) + tmp;

        if (l === r) {
            return data[l];
        }

        let lVal = data[l];
        let rVal = data[r];

        while (Math.floor(l/2) !== Math.floor(r/2)) {
            if (l % 2 === 0 && l + 1 <= r) {
                lVal = Math.max(lVal, data[l+1]);
            }
            l = Math.floor(l / 2);
            if (r % 2 === 1 && r-1 >= l) {
                rVal = Math.max(rVal, data[r-1]);
            }
            r = Math.floor(r / 2);
        }

        return Math.max(lVal, rVal);
    }

    for (let i = 0; i < n; i++) {
        update(i, heights[i]);
    }

    const ans = [];
    for (let i = 0; i < queries.length; i++) {
        let [a, b] = queries[i];
        if (a === b) {
            ans.push(a);
            continue;
        } else if (a > b) {
            const tmp = a;
            a = b;
            b = tmp;
        }
        if (heights[a] < heights[b]) {
            ans.push(b);
            continue;
        }
        if (b === n -1) {
            ans.push(-1);
            continue;
        }
        let l = b+1;
        let r = n-1;
        if (heights[a] >= query(l, r) || heights[b] >= query(l, r)) {
            ans.push(-1);
            continue;
        }
        while (l + 1 < r) {
            const m = l + Math.floor((r - l) / 2);
            if (heights[a] < query(l, m) && heights[b] < query(l, m)) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        if (heights[a] < heights[l] && heights[b] < heights[l]) {
            ans.push(l);
        } else {
            ans.push(r);
        }
    }

    return ans;
};
