function minimumPushes(word: string): number {
    const counter = Array(26).fill(0);
    for (let i = 0; i < word.length; i++) {
        counter[word.charCodeAt(i) - 'a'.charCodeAt(0)]++;
    }
    counter.sort((a, b) => b - a);
    let ans = 0;
    for (let i = 0; i < 26; i++) {
        ans += counter[i] * (Math.floor(i / 8) + 1);
    }
    return ans;
};
