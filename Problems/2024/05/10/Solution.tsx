function kthSmallestPrimeFraction(arr: number[], k: number): number[] {
    const nums = [];
    for (let i = 0; i < arr.length-1; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            nums.push([arr[i]/arr[j], arr[i], arr[j]]);
        }
    }
    nums.sort((a, b) => a[0] - b[0]);
    return [nums[k-1][1], nums[k-1][2]];
};
