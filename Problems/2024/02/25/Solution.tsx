function canTraverseAllPairs(nums: number[]): boolean {
    if (nums.length === 1) {
        return true;
    }
    if (nums.includes(1)) {
        return false;
    }

    function primeFactorize(num: number): number[] {
        const primes = new Set<number>();
        for (let i = 2; Math.pow(i, 2) <= num; i++) {
            while (num % i === 0) {
                primes.add(i);
                num /= i;
            }
        }
        if (num > 1) {
            primes.add(num);
        }
        return Array.from(primes.values());
    }

    const arr: number[][] = nums.map(num => primeFactorize(num));
    const ids = new Map<number, number>();
    for (const primes of arr) {
        for (const p of primes) {
            if (!ids.has(p)) {
                ids.set(p, p);
            }
        }
    }

    const find = u => {
        if (ids.get(u) !== u) {
            ids.set(u, find(ids.get(u)));
        }
        return ids.get(u);
    }

    const union = (u, v) => {
        u = find(u);
        v = find(v);
        ids.set(u, v);
    }

    for (const primes of arr) {
        for (let i = 1; i < primes.length; i++) {
            union(primes[i-1], primes[i]);
        }
    }

    const group = new Set();
    for (const v of ids.values()) {
        group.add(find(v));
    }

    return group.size === 1;
};
