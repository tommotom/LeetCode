function findKthNumber(n: number, k: number): number {
    const countSteps = (n, p1, p2) => {
        let steps = 0;
        while (p1 <= n) {
            steps += Math.min(n+1, p2) - p1;
            p1 *= 10;
            p2 *= 10;
        }
        return steps;
    }

    let cur = 1;
    k--;

    while (k > 0) {
        const step = countSteps(n, cur, cur + 1);
        if (step <= k) {
            cur++;
            k -= step;
        } else {
            cur *= 10;
            k--;
        }
    }

    return cur;
};
