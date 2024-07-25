function sortArray(nums: number[]): number[] {
    const mergeSort = arr => {
        const n = arr.length;
        if (n === 1) {
            return arr;
        }
        const m = Math.floor(n / 2);

        const left = mergeSort(arr.slice(0, m));
        const right = mergeSort(arr.slice(m, n));

        const ret = [];
        let l = 0, r = 0;
        while (l < left.length && r < right.length) {
            if (left[l] < right[r]) {
                ret.push(left[l++]);
            } else {
                ret.push(right[r++]);
            }
        }
        while (l < left.length) {
            ret.push(left[l++]);
        }
        while (r < right.length) {
            ret.push(right[r++]);
        }

        return ret;
    }

    return mergeSort(nums);
};
