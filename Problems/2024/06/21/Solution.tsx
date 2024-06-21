function maxSatisfied(customers: number[], grumpy: number[], minutes: number): number {
    const n = customers.length;
    let diff = 0, satisfied = 0;
    for (let i = 0; i < Math.min(n, minutes); i++) {
        satisfied += customers[i] * (1 - grumpy[i]);
        diff += customers[i] * grumpy[i];
    }

    let max = diff;
    for (let i = minutes; i < n; i++) {
        satisfied += customers[i] * (1 - grumpy[i]);
        diff += customers[i] * grumpy[i];
        diff -= customers[i-minutes] * grumpy[i-minutes];
        max = Math.max(max, diff);
    }

    return satisfied + max;
};
