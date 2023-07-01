function distributeCookies(cookies: number[], k: number): number {
    cookies.sort((a, b) => a - b);

    let ans = cookies.reduce((a, b) => a + b);
    const cur = new Array(k);
    for (let i = 0; i < k; i++) {
        cur[i] = 0;
    }

    const backTrack = (i: number): void => {
        const score = cur.reduce((a, b) => Math.max(a, b));
        if (i === cookies.length) {
            ans = Math.min(ans, score);
            return;
        }
        if (score > ans) {
            return;
        }
        for (let j = 0; j < k; j++) {
            cur[j] += cookies[i];
            backTrack(i+1);
            cur[j] -= cookies[i];
            if (cur[j] === 0) {break;}
        }
    };

    backTrack(0);

    return ans;
};