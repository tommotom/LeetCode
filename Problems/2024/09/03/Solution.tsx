function getLucky(s: string, k: number): number {
    const convert = s => s.split('').map(c => c.charCodeAt(0) - 'a'.charCodeAt(0) + 1).join('');
    const transform = num => {
        let ret = 0;
        for (let i = 0; i < num.length; i++) {
            ret += Number(num.charAt(i));
        }
        return ret.toString();
    }
    let ans = convert(s);
    for (let _ = 0; _ < k; _++) {
        ans = transform(ans);
    }
    return Number(ans);
};
