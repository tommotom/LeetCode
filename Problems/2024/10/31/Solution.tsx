function minimumTotalDistance(robot: number[], factory: number[][]): number {
    robot.sort((a, b) => a - b);
    factory.sort((a, b) => a[0] - b[0]);
    const memo = new Map();
    const helper = (i, j, k) => {
        if (i === robot.length) {
            return 0;
        }
        if (j === factory.length) {
            return Number.MAX_SAFE_INTEGER;
        }
        const key = `${i}, ${j}, ${k}`;
        if (!memo.has(key)) {
            const res1 = helper(i, j+1, 0);
            const res2 = factory[j][1] > k ? helper(i+1, j, k+1) + Math.abs(robot[i] - factory[j][0]) : Number.MAX_SAFE_INTEGER;
            memo.set(key, Math.min(res1, res2));
        }
        return memo.get(key);
    }
    return helper(0, 0, 0);
};
