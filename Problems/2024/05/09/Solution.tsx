function maximumHappinessSum(happiness: number[], k: number): number {
    happiness.sort((a, b) => b - a);
    let ans = 0;
    for (let i = 0; i < k; i++) {
        ans += Math.max(0, happiness[i] - i);
    }
    return ans;
};
