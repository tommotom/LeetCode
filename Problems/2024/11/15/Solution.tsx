function findLengthOfShortestSubarray(arr: number[]): number {
    let r = arr.length - 1;
    while (r > 0 && arr[r-1] <= arr[r]) {
        r--;
    }

    let ans = r, l = 0;
    while (l < r && (l === 0 || arr[l-1] <= arr[l])) {
        while (r < arr.length && arr[l] > arr[r]) {
            r++;
        }
        ans = Math.min(ans, r - l - 1);
        l++;
    }

    return ans;
};
