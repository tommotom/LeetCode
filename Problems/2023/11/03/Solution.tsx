function buildArray(target: number[], n: number): string[] {
    let i = 0;
    const ans = [];
    for (let num = 1; num <= n && i < target.length; num++) {
        ans.push("Push");
        if (target[i] === num) {
            i++;
        } else {
            ans.push("Pop");
        }
    }
    return ans;
};
