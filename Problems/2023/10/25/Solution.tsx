function kthGrammar(n: number, k: number): number {
    const b = "00000000000000000000" + ((k-1) >>> 0).toString(2);
    let num = 0;
    for (let i = 0; i < n-1; i++) {
        if (b.charAt(b.length-n+1+i) === '1') {
            num = num === 0 ? 1 : 0;
        }
    }
    return num;
};
