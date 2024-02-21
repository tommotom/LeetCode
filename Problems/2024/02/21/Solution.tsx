function rangeBitwiseAnd(left: number, right: number): number {
    let ans = 0;
    for (let bit = 31; bit >= 0; bit--) {
        if ((left & (1 << bit)) === (right & (1 << bit))) {
            ans += (left & (1 << bit));
        } else {
            break;
        }
    }
    return ans;
};