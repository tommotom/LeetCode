function countBits(n: number): number[] {
    return [...Array(n+1)].map((_, num) => num.toString(2).split('1').length-1);
};
