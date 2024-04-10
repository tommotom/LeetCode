function deckRevealedIncreasing(deck: number[]): number[] {
    const n = deck.length;
    deck.sort((a, b) => a - b);
    let i = 0, seats = Array.from(Array(n).keys());
    const ans = Array(n);
    while (i < n) {
        let j = 0;
        const next = [];
        while (j < seats.length) {
            ans[seats[j++]] = deck[i++];
            if (j < seats.length) {
                next.push(seats[j++]);
            } else if (next.length > 0) {
                next.push(next.shift());
            }
        }
        seats = next;
    }
    return ans;
};
