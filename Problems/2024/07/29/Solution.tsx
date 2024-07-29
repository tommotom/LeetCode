function numTeams(rating: number[]): number {
    let ans = 0;
    for (let j = 1; j < rating.length - 1; j++) {
        let ll = 0, lg = 0;
        for (let i = 0; i < j; i++) {
            if (rating[i] < rating[j]) {
                ll++;
            } else if (rating[i] > rating[j]) {
                lg++;
            }
        }

        let rl = 0, rg = 0;
        for (let k = j+1; k < rating.length; k++) {
            if (rating[j] < rating[k]) {
                rg++;
            } else if (rating[j] > rating[k]) {
                rl++;
            }
        }

        ans += ll * rg;
        ans += lg * rl;
    }

    return ans;
};
