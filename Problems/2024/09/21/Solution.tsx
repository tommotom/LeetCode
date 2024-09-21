function lexicalOrder(n: number): number[] {
    const arr = [], ans = [];
    const nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    const helper = i => {
        if (i === 10) {
            return;
        }
        arr.push(nums[i]);
        const num = Number(arr.join(''));
        if (1 <= num && num <= n) {
            ans.push(num);
            helper(0);
        }
        arr.pop();
        helper(i+1);
    }
    helper(1);
    return ans;
};
