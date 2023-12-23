function isPathCrossing(path: string): boolean {
    const dir: Map<string, [number, number]> = new Map([
        ['N', [0,1]], ['S', [0,-1]], ['E', [1,0]], ['W', [-1,0]]
    ]);
    const visited: Set<string> = new Set(["0,0"]);
    let x = 0, y = 0;
    for (const c of path) {
        x += dir.get(c)[0];
        y += dir.get(c)[1];
        const key = x + "," + y;
        if (visited.has(key)) {
            return true;
        }
        visited.add(key);
    }
    return false;
};
