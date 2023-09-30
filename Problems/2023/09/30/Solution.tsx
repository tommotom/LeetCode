function find132pattern(nums: number[]): boolean {
    const stack = [];
    let third = Number.MIN_SAFE_INTEGER;

    for (const num of nums.reverse()) {
        if (num < third) {
            return true;
        }
        while (stack.length > 0 && stack[stack.length-1] < num) {
            third = stack.pop();
        }
        stack.push(num);
    }

    return false;
};
