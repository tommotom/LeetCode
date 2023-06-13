function equalPairs(grid: number[][]): number {
    const counter: Map<string, number> = new Map();
    for (let i = 0; i < grid.length; i++) {
        const key: string = grid[i].join(',');
        if (!counter.has(key)) {
            counter.set(key, 0);
        }
        counter.set(key, counter.get(key) + 1);
    }

    let ans: number = 0;
    for (let i = 0; i < grid.length; i++) {
        const arr: Array<number> = new Array();
        for (let j = 0; j < grid[i].length; j++) {
            arr.push(grid[j][i]);
        }
        const key: string = arr.join(',');
        if (counter.has(key)) {
            ans += counter.get(key);
        }
    }

    return ans;
}
