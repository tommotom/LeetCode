function combine(n: number, k: number): number[][] {
    const ans: number[][] = [];

    function helper(num: number, arr: number[]) {
        if (arr.length === k) {
            ans.push([...arr]);
            return;
        }
        if (num > n) {
            return;
        }
        helper(num+1, arr);
        arr.push(num);
        helper(num+1, arr);
        arr.pop();
    }

    helper(1, []);

    return ans;
};
