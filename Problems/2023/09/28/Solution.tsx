function sortArrayByParity(nums: number[]): number[] {
    nums.sort((a, b) => a%2 - b%2);
    return nums;
};
