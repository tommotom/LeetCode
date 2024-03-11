function customSortString(order: string, s: string): string {
    const o = new Map();
    for (let i = 0; i < order.length; i++) {
        o.set(order.charAt(i), i);
    }
    for (let i = 0; i < s.length; i++) {
        if (!o.has(s.charAt(i))) {
            o.set(s.charAt(i), s.length);
        }
    }
    return [...s].sort((a, b) => o.get(a) - o.get(b)).join('');
};
