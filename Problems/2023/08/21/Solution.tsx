function repeatedSubstringPattern(s: string): boolean {
    for (let i = 1; i <= Math.floor(s.length/2); i++) {
        const substr = s.substring(0, i);
        if (s.length % substr.length !== 0) {
            continue;
        }
        let j = i;
        while (j+substr.length <= s.length) {
            if (s.substring(j, j+substr.length) !== substr) {
                break;
            }
            j += substr.length;
        }
        if (j+substr.length > s.length) {
            return true;
        }
    }
    return false;
};
