function getLastMoment(n: number, left: number[], right: number[]): number {
    return Math.max(
        left.length > 0 ? left.reduce((a, b) => Math.max(a, b)) : 0,
        right.length > 0 ? n - right.reduce((a, b) => Math.min(a, b)) : 0
    );
};
