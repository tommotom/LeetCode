function largestCombination(candidates: number[]): number {
    const counter = Array(32).fill(0);
    for (let num of candidates) {
        let bit = 0;
        while (num > 0) {
            counter[bit] += num % 2;
            num = Math.floor(num / 2);
            bit++;
        }
    }
    return counter.reduce((a, b) => Math.max(a, b));
};
