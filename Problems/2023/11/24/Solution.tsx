function maxCoins(piles: number[]): number {
    piles.sort((a, b) => a - b);
    let ans = 0;
    for (let i = 0; i < piles.length / 3; i++) {
        ans += piles[piles.length - (i+1) * 2];
    }
    return ans;
};
