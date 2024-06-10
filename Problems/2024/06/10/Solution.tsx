function heightChecker(heights: number[]): number {
    return heights.concat()
        .sort((a, b) => a - b)
        .filter((e, i, arr) => e !== heights[i])
        .length;
};
