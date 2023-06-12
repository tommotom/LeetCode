function summaryRanges(nums: number[]): string[] {
    if (nums.length === 0) {return [];}
    const ret: string[] = [];
    let l: number = 0;
    for (let r: number = 0; r < nums.length; r++) {
        if (r+1 < nums.length && nums[r] + 1 === nums[r+1]) {
            continue;
        }
        if (l === r) {
            ret.push(nums[l].toString());
        } else {
            ret.push(`${nums[l]}->${nums[r]}`);
        }
        l = r + 1;
    }
    return ret;
}
