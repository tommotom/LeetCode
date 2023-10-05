function majorityElement(nums: number[]): number[] {
    let candidate1 = 0, candidate2 = 1, count1 = 0, count2 = 0;
    for (const num of nums) {
        if (candidate1 === num) {
            count1++;
        } else if (candidate2 === num) {
            count2++;
        } else if (count1 === 0) {
            candidate1 = num, count1 = 1;
        } else if (count2 === 0) {
            candidate2 = num, count2 = 1;
        } else {
            count1--, count2--;
        }
    }
    count1 = 0, count2 = 0;
    for (const num of nums) {
        if (candidate1 === num) {
            count1++;
        } else if (candidate2 === num) {
            count2++;
        }
    }
    const ans = [];
    if (count1 > nums.length / 3) {
        ans.push(candidate1);
    }
    if (count2 > nums.length / 3) {
        ans.push(candidate2);
    }
    return ans;
};
