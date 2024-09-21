function largestNumber(nums: number[]): string {
    const strNums = nums.map(num => num.toString()).sort((a, b) => Number(b + a) - Number(a + b));
    if (strNums[0] === "0") {
        return "0";
    }
    return strNums.join("");
};
