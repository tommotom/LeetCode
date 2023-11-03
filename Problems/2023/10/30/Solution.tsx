function sortByBits(arr: number[]): number[] {
    function numOf1Bits(num: number): number {
        let count = 0;
        while (num > 0) {
            count += num % 2;
            num >>= 1
        }
        return count;
    }
    arr.sort((a, b) => numOf1Bits(a) === numOf1Bits(b) ? a - b : numOf1Bits(a) - numOf1Bits(b));
    return arr;
};
