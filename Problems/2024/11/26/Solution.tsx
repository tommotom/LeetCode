function findChampion(n: number, edges: number[][]): number {
    const weaker = Array(n).fill(0);
    for (const [a, b] of edges) {
        weaker[b]++;
    }
    let winner = -1;
    for (let i = 0; i < n; i++) {
        if (weaker[i] === 0) {
            if (winner >= 0) {
                return -1;
            }
            winner = i;
        }
    }
    return winner;
};
