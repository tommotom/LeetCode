function numFactoredBinaryTrees(arr: number[]): number {
    arr.sort((a, b) => a - b);
    const visited = new Set();
    const product = new Map();
    for (const num of arr) {
        for (const a of arr) {
            if (a === num) {
                break;
            }
            const b = num / a;
            if (visited.has(b)) {
                if (!product.has(num)) {
                    product.set(num, []);
                }
                product.get(num).push([a, b]);
            }
        }
        visited.add(num);
    }

    const mod = 1000000007;
    const memo = new Map();
    function helper(root) {
        if (memo.has(root)) {
            return memo.get(root);
        }
        let ret = 1;
        for (const [a, b] of product.get(root) || []) {
            ret += helper(a) * helper(b);
            ret %= mod;
        }
        memo.set(root, ret);
        return ret;
    }

    let ans = 0;
    for (const num of arr) {
        ans += helper(num);
        ans %= mod
    }
    return ans;
};
