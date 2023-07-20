function asteroidCollision(asteroids: number[]): number[] {
    const ans: number[] = [];
    for (const asteroid of asteroids) {
        if (asteroid > 0) {
            ans.push(asteroid);
            continue;
        }
        let broke = false;
        while (ans.length > 0 && ans[ans.length-1] > 0) {
            const target = ans[ans.length-1];
            if (target <= Math.abs(asteroid)) {
                ans.pop();
            }
            if (target >= Math.abs(asteroid)) {
                broke = true;
                break;
            }
        }
        if (!broke) {
            ans.push(asteroid);
        }
    }
    return ans;
};
