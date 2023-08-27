function canCross(stones: number[]): boolean {

    const map = new Map();
    for (let i = 0; i < stones.length; i++) {
        map.set(stones[i], i);
    }

    const tried = new Set();
    function helper(i: number, k: number) {
        if (i === stones.length-1) {
            return true;
        }
        const key = i.toString() + " " + k.toString();
        if (tried.has(key)) {
            return false;
        }
        for (let j = Math.max(1, k-1); j <= k+1; j++) {
            if (map.has(stones[i] + j)) {
                const nextI = map.get(stones[i] + j);
                if (helper(nextI, stones[nextI] - stones[i])) {
                    return true;
                }
            }
        }
        tried.add(key);
        return false;
    }

    if (stones[1] !== 1) {
        return false;
    }

    return helper(1, 1);
};
