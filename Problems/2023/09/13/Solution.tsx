function candy(ratings: number[]): number {
    const n = ratings.length, arr = [];
    for (let i = 0; i < n; i++) {
        arr.push([i, ratings[i]]);
    }
    arr.sort((a, b) => a[1] - b[1]);

    const candy = [...Array(n)].map(_ => 0);
    for (const [i, r] of arr) {
        let c = 1;
        if (i > 0 && ratings[i] > ratings[i-1]) {
            c = Math.max(c, candy[i-1] + 1);
        }
        if (i+1 < n && ratings[i] > ratings[i+1]) {
            c = Math.max(c, candy[i+1] + 1);
        }
        candy[i] = c;
    }

    return candy.reduce((a, b) => a + b);
};
