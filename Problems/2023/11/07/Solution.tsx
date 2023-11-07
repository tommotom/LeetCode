function eliminateMaximum(dist: number[], speed: number[]): number {
    const reachAt = [];
    for (let i = 0; i < dist.length; i++) {
        reachAt.push(dist[i] / speed[i]);
    }
    reachAt.sort((a, b) => a - b);

    for (let i = 0; i < dist.length; i++) {
        if (reachAt[i] <= i) {
            return i;
        }
    }
    return reachAt.length;
};
