function makeArrayIncreasing(arr1: number[], arr2: number[]): number {
    arr2 = arr2.sort((n1,n2) => n1 - n2);

    const memo: Map<number, Map<number, number>> = new Map();
    function helper(i: number, prev: number) {
        if (i === arr1.length) { return 0; }
        if (memo.has(i) && memo.get(i).has(prev)) {
            return memo.get(i).get(prev);
        }
        let ret: number = Number.MAX_SAFE_INTEGER;
        if (prev < arr1[i]) {
            ret = helper(i+1, arr1[i]);
        }

        let l: number = 0, r: number = arr2.length;
        while (l < r) {
            const m: number = Math.floor(l + (r - l) / 2);
            if (arr2[m] <= prev) {
                l = m + 1;
            } else {
                r = m;
            }
        }

        if (l < arr2.length) {
            ret = Math.min(ret, helper(i+1, arr2[l]) + 1);
        }

        if (!memo.has(i)) {
            memo.set(i, new Map());
        }
        memo.get(i).set(prev, ret);
        return ret;
    }

    return helper(0, -1) === Number.MAX_SAFE_INTEGER ? -1 : helper(0, -1);
};
