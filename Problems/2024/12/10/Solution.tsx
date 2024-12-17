function maximumLength(s: string): number {
    const isSpecial = s => {
        const a = s.charAt(0);
        for (const c of s.slice('')) {
            if (a !== c) {
                return false;
            }
        }
        return true;
    }

    const counter = new Map();
    for (let i = 0; i < s.length; i++) {
        for (let j = i + 1; j <= s.length; j++) {
            const substr = s.substring(i, j)
            if (isSpecial(substr)) {
                if (!counter.has(substr)) {
                    counter.set(substr, 0);
                }
                counter.set(substr, counter.get(substr) + 1);
            }
        }
    }
    let length = -1;
    for (const [k, v] of counter.entries()) {
        if (v >= 3) {
            length = Math.max(length, k.length);
        }
    }

    return length;
};
