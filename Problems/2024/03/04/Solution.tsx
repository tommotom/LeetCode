function bagOfTokensScore(tokens: number[], power: number): number {
    tokens.sort((a, b) => a - b);
    let score = 0, ans = 0, i = 0;
    for (let j = tokens.length-1; j >= 0; j--) {
        while(i <= j && tokens[i] <= power) {
            power -= tokens[i++];
            score++;
        }
        ans = Math.max(ans, score);
        if (i > j) {
            break;
        }
        if (score > 0) {
            power += tokens[j];
            score--;
        }
    }
    return ans;
};
