function longestCommonPrefix(arr1: number[], arr2: number[]): number {
    const set = new Set();
    for (const num of arr1.map(num => num.toString())) {
        for (let i = 1; i <= num.length; i++) {
            set.add(num.substring(0, i));
        }
    }
    let ans = 0;
    for (const num of arr2.map(num => num.toString())) {
        for (let i = 1; i <= num.length; i++) {
            if (set.has(num.substring(0, i))) {
                ans = Math.max(ans, i);
            }
        }
    }
    return ans;
};
