function findDifferentBinaryString(nums: string[]): string {
    const n = nums.length;
    function numToBin(num: number):string {
        const arr = [];
        for (let i = 0; i < n; i++) {
            arr.push((num % 2).toString());
            num >>= 1;
            console.log(num)
        }
        return arr.reverse().join('');
    }

    nums.sort();
    let num = 0;
    for (let i = 0; i < Math.pow(2, n); i++) {
        if (numToBin(num) !== nums[i]) {
            return numToBin(num);
        }
        num++;
    }
    return "0"
};
