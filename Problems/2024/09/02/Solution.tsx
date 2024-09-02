function chalkReplacer(chalk: number[], k: number): number {
    const sum = chalk.reduce((a, b) => a + b);
    k %= sum;
    for (let i = 0; i < chalk.length; i++) {
        if (k < chalk[i]) {
            return i;
        }
        k -= chalk[i];
    }
    return 0;
};
