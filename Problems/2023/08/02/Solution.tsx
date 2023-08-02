function permute(nums: number[]): number[][] {
    const n = nums.length;
    const used: boolean[] = [...Array(n)].map((_) => false);
    const ans: number[][] = [];
    const arr: number[] = [];

    function helper(): void {
        if (arr.length === n) {
            ans.push([...arr]);
            return;
        }
        for (let i = 0; i < n; i++) {
            if (!used[i]) {
                used[i] = true;
                arr.push(nums[i]);
                helper();
                arr.pop();
                used[i] = false;
            }
        }
    }

    helper();
    return ans;
};
