function findTheWinner(n: number, k: number): number {
    const friends = Array(n).fill(0).map((_, i) => i);
    let i = 0;
    while (n > 1) {
        i = (i + k - 1) % n;
        friends.splice(i, 1);
        n -= 1;
    }
    return friends[0] + 1;
};
