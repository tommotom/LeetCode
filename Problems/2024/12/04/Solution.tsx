function canMakeSubsequence(str1: string, str2: string): boolean {
    const toNum = c => c.charCodeAt(0) - 'a'.charCodeAt(0);
    const m = str1.length, n = str2.length;
    let j = 0;

    for (let i = 0; i < m; i++) {
        const c1 = str1.charAt(i), c2 = str2.charAt(j);
        if (j < n && (c1 === c2 || (toNum(c1) + 1) % 26 === toNum(c2))) {
            j++;
        }
    }

    return j === n;
};
