function canSortArray(nums: number[]): boolean {
    const count = num => {
        let bit = 0;
        while (num > 0) {
            bit += num % 2;
            num = Math.floor(num / 2);
        }
        return bit;
    }
    const setBits = nums.map(num => count(num));

    const devided = [];
    let tmp = [nums[0]];
    for (let i = 1; i < nums.length; i++) {
        if (setBits[i-1] !== setBits[i]) {
            devided.push(tmp);
            tmp = [];
        }
        tmp.push(nums[i]);
    }

    nums.sort((a, b) => a - b);
    let i = 0;
    for (const arr of devided) {
        for (const num of arr.sort((a, b) => a - b)) {
            if (num !== nums[i]) {
                return false;
            }
            i++;
        }
    }
    return true;
};
