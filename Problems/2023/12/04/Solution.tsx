function largestGoodInteger(num: string): string {
    let ans = "";
    let i = 0;
    while (i < num.length) {
        let j = i + 1;
        while (j < num.length && j < i + 3 && num.charAt(i) === num.charAt(j)) {
            if (num.charAt(i) !== num.charAt(j)) {
                i = j;
            } else {
                j++;
            }
        }
        if (j === i + 3 && ans < num.substring(i, j)) {
            ans = num.substring(i, j);
        }
        i++;
    }
    return ans;
};
