function maxDistance(position: number[], m: number): number {
    position.sort((a, b) => a - b);

    const helper = (mid) => {
        let count = 1, last = position[0];
        for (let i = 1; i < position.length; i++) {
            if (position[i] - last >= mid) {
                last = position[i];
                count++;
            }
        }
        return count;
    }


    let l = 1, r = position[position.length-1];
    while (l < r) {
        const mid = l + Math.floor((r - l) /2);
        if (helper(mid) < m) {
            r = mid
        } else {
            l = mid + 1;
        }
    }

    return l - 1;
};
