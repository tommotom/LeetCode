function winnerOfGame(colors: string): boolean {
    let alice = 0, bob = 0;
    for (let i = 1; i < colors.length-1; i++) {
        if (colors.charAt(i-1) === colors.charAt(i) && colors.charAt(i) === colors.charAt(i+1)) {
            alice += colors.charAt(i) === 'A' ? 1 : 0;
            bob += colors.charAt(i) === 'B' ? 1 : 0;
        }
    }
    return alice > bob;
};
