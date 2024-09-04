function robotSim(commands: number[], obstacles: number[][]): number {
    const toString = (x, y) => `${x},${y}`;

    const set = new Set();
    for (const [x, y] of obstacles) {
        set.add(toString(x, y));
    }

    const dirs = [[0,1], [1,0], [0,-1],[-1,0]];
    let d = 0, x = 0, y = 0, ans = 0;
    for (const c of commands) {
        if (c === -2) {
            d = d === 0 ? 3 : d-1;
        } else if (c === -1) {
            d = (d + 1) % 4;
        } else {
            const [dx, dy] = dirs[d];
            for (let _ = 0; _ < c; _++) {
                const nextX = x + dx, nextY = y + dy;
                if (set.has(toString(nextX, nextY))) {
                    break;
                }
                x = nextX;
                y = nextY;
            }
        }
        ans = Math.max(ans, x * x + y * y);
    }

    return ans;
};
