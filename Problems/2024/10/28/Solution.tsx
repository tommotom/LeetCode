class Node {
    val: number;
    next: Node;

    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

function longestSquareStreak(nums: number[]): number {
    nums.sort((a, b) => b - a);
    const set = new Set(nums);
    const nodes = new Map();
    for (const num of nums) {
        const node = new Node(num);
        if (set.has(num * num)) {
            node.next = nodes.get(num * num);
        }
        nodes.set(num, node);
    }

    const memo = new Map();
    const dfs = node => {
        if (!memo.has(node.val)) {
            memo.set(node.val, node.next === null ? 1 : dfs(node.next) + 1);
        }
        return memo.get(node.val);
    }

    for (const node of nodes.values()) {
        dfs(node);
    }

    let ans = 0;
    for (const val of memo.values()) {
        ans = Math.max(ans, val);
    }

    return ans === 1 ? -1 : ans;
};
