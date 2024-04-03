function isIsomorphic(s: string, t: string): boolean {
    const map = new Map();
    for (let i = 0; i < s.length; i++) {
        if (!map.has(s.charAt(i))) {
            map.set(s.charAt(i), t.charAt(i));
        }
        if (map.get(s.charAt(i)) !== t.charAt(i)) {
            return false;
        }
    }

    const reverse = new Map();
    let isValid = true
    map.forEach((v, k) => {
        if (!reverse.has(v)) {
            reverse.set(v, k);
        } else if (reverse.get(v) !== k) {
            isValid = false;
        }

    });
    return isValid;
};
