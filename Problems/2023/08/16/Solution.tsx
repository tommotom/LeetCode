function maxSlidingWindow(nums: number[], k: number): number[] {
    const q = [], ans = [];
    for (let i = 0; i < nums.length; i++) {
        while (q.length > 0 && q[0] < i - k + 1) {q.shift();}
        while (q.length > 0 && nums[q[q.length-1]] < nums[i]) {q.pop();}
        q.push(i);
        if (i+1 >= k) {ans.push(nums[q[0]]);}
    }
    return ans;
};
