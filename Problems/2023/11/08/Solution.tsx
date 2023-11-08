function isReachableAtTime(sx: number, sy: number, fx: number, fy: number, t: number): boolean {
    if (t === 1 && sx === fx && sy === fy) {
        return false;
    }
    const diagonal = Math.min(Math.abs(sx - fx), Math.abs(sy - fy));
    const straight = Math.max(Math.abs(sx - fx), Math.abs(sy - fy)) - diagonal;
    return diagonal + straight <= t;
};
