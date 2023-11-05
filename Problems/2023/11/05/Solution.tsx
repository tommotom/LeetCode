function getWinner(arr: number[], k: number): number {
    if (k >= arr.length) {
        return arr.reduce((a, b) => Math.max(a, b));
    }
    let winner = arr.shift(), count = 0;
    while (true) {
        const challenger = arr.shift();
        if (winner > challenger) {
            arr.push(challenger);
            count++;
        } else {
            arr.push(winner);
            winner = challenger;
            count = 1;
        }
        if (count === k) {
            return winner;
        }
    }
};
