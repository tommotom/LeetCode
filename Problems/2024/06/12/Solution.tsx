/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
    let l = 0, m = 0, r = nums.length-1;
    while (m <= r) {
        if (nums[m] === 0) {
            const tmp = nums[l];
            nums[l] = nums[m];
            nums[m] = tmp;
            l++;
            m++;
        } else if (nums[m] === 1) {
            m++;
        } else {
            const tmp = nums[r];
            nums[r] = nums[m];
            nums[m] = tmp;
            r--;
        }
    }
};
