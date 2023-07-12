function maxConsecutiveAnswers(answerKey: string, k: number): number {
    let l = 0, r = 0;
    let t = 0, f = 0, ans = 0;
    while (l < answerKey.length) {
        if (r < answerKey.length && Math.min(t, f) <= k) {
            if (answerKey.charAt(r++) === "T") {
                t++;
            } else {
                f++;
            }
        } else {
            if (answerKey.charAt(l++) === "T") {
                t--;
            } else {
                f--;
            }
        }
        if (Math.min(t, f) <= k) {
            ans = Math.max(ans, t + f);
        }
    }
    return ans;
};
