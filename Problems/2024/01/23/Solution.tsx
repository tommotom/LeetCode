function maxLength(arr: string[]): number {
    let ans = 0;
    for (let bit = 0; bit < Math.pow(2, arr.length); bit++) {
        const set = new Set();
        let isValid = true;
        for (let i = 0; i < arr.length; i++) {
            if (((1 << i) & bit) === 0) {
                continue;
            }
            for (const char of arr[i]) {
                if (set.has(char)) {
                    isValid = false;
                }
                set.add(char);
            }
        }
        if (isValid) {
            ans = Math.max(ans, set.size);
        }
    }
    return ans;
};
