function groupAnagrams(strs: string[]): string[][] {

    function keyOf(str: string): string {
        const counter = Array(26).fill(0);
        for (const c of str) {
            counter[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
        }
        return counter.map((num) => num.toString()).join(',');
    }

    const group = new Map();
    for (const str of strs) {
        const key = keyOf(str);
        if (!group.has(key)) {
            group.set(key, []);
        }
        group.get(key).push(str);
    }

    return [...group.values()];
};
