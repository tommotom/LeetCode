function majorityElement(nums: number[]): number {
    let count = 0, element = 0;
    for (const num of nums) {
        if (count === 0) {
            element = num;
        }
        count += element === num ? 1 : -1;
    }
    return element;
};
