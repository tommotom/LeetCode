function productExceptSelf(nums: number[]): number[] {
    const left = [1];
    for (const num of nums) {
        left.push(left[left.length-1] * num);
    }

    const right = [1];
    nums.reverse();
    for (const num of nums) {
        right.push(right[right.length-1] * num);
    }
    right.reverse();

    const ans = [];
    for (let i = 0; i < nums.length; i++) {
        ans.push(left[i] * right[i+1]);
    }
    return ans;
};
