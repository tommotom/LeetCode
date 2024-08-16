function maxDistance(arrays: number[][]): number {
    const mins = [], maxs = [];
    for (let i = 0; i < arrays.length; i++) {
        mins.push([arrays[i][0], i]);
        maxs.push([arrays[i][arrays[i].length-1], i]);
    }
    mins.sort((a, b) => a[0] - b[0]);
    maxs.sort((a, b) => b[0] - a[0]);

    if (maxs[0][1] !== mins[0][1]) {
        return maxs[0][0] - mins[0][0];
    }

    return Math.max(maxs[0][0] - mins[1][0], maxs[1][0] - mins[0][0]);
};
