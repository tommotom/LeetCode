function peakIndexInMountainArray(arr: number[]): number {
    let l = 1, r = arr.length-1;
    while (l < r) {
        const m = l + Math.floor((r - l) / 2);
        if (arr[m-1] < arr[m] && arr[m] > arr[m+1]) {
            return m;
        } else if (arr[m] < arr[m+1]) {
            l = m + 1;
        } else if (arr[m-1] > arr[m]) {
            r = m - 1;
        }
    }
    return l;
};
