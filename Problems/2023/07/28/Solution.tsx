function PredictTheWinner(nums: number[]): boolean {
    function helper(i: number, j: number, score: number, sign: number) {
        if (i > j) {
            return score >= 0;
        }
        const first = helper(i+1, j, score + nums[i] * sign, sign * -1);
        const last = helper(i, j-1, score + nums[j] * sign, sign * -1);
        return sign === 1 ? first || last : first && last;
    }
    return helper(0, nums.length - 1, 0, 1);
};
